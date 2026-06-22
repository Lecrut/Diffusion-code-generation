class ActionRepeater:
    MAX_RETRIES = 25

    @staticmethod
    def perform_action():
        try:
            print('Action executed')
        except Exception as e:
            print(f'Error during action: {e}')

if __name__ == '__main__':
    repeater = ActionRepeater()
    for _ in range(ActionRepeater.MAX_RETRIES):
        repeater.perform_action()