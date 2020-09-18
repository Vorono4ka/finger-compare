import json
import os


class Checker:
    def __init__(self, previous_finger: dict, current_finger: dict):
        self.previous_finger = previous_finger
        self.current_finger = current_finger

    def check_files(self):
        changed = []
        removed = []
        added = []

        previous_files = self.previous_finger['files']
        current_files = self.current_finger['files']

        previous_file_paths = [file['file'] for file in previous_files]
        current_file_paths = [file['file'] for file in current_files]

        for file in current_files:
            if file in previous_files:
                continue
            else:
                file_path = file['file']
                if file_path in previous_file_paths:
                    changed.append(file)
                else:
                    added.append(file)

        for file_path in previous_file_paths:
            if file_path not in current_file_paths:
                removed.append(file_path)

        result = {
            'changed': changed,
            'removed': removed,
            'added': added
        }

        return result


if __name__ == '__main__':
    if not os.path.exists('main-data'):
        os.mkdir('main-data')

    with open('main-data/28.233.1.json') as previous_finger_file:
        previous_finger_data = json.load(previous_finger_file)
        previous_finger_file.close()
    with open('main-data/29.272.1.json') as current_finger_file:
        current_finger_data = json.load(current_finger_file)
        current_finger_file.close()

    checker = Checker(previous_finger_data,
                      current_finger_data)

    _result = checker.check_files()

    _changed = _result['changed']
    _removed = _result['removed']
    _added = _result['added']

    print(
        f'Changed: {len(_changed)} files\n'
        f'Removed: {len(_removed)} files\n'
        f'Added: {len(_added)} files'
    )
