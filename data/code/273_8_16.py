import time

class ActionRepeater:
    def execute_action(self):
        print('Action executed')

def repeat_sequence(action_func):
    repeater = ActionRepeater()
    for _ in range(3):
        action_func()
        time.sleep(1)
        repeater.execute_action()

if __name__ == '__main__':
    perform_action = lambda: print('Action executed')
    repeat_sequence(perform_action)