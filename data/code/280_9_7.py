class ActionRepeater:
    MAX_REPETITIONS = 25

    @staticmethod
    def execute_action():
        try:
            print('Action executed')
        except Exception as e:
            print(f'Error during action: {e}')

if __name__ == '__main__':
    repeater = ActionRepeater()
    for _ in range(ActionRepeater.MAX_REPETITIONS):
        repeater.execute_action()