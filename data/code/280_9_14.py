class ActionRepeater:
    MAX_ITERATIONS = 25

    @staticmethod
    def execute_action():
        print('Action executed')

    @classmethod
    def repeat_actions(cls):
        for _ in range(cls.MAX_ITERATIONS):
            try:
                cls.execute_action()
            except Exception as e:
                print(f'Error during action: {e}')

if __name__ == '__main__':
    ActionRepeater.repeat_actions()