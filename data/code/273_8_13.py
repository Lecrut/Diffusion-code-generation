import time

class ActionRepeater:
    def execute_action(self):
        print('Action executed')

def repeat_sequence(action_func, N=3):
    for _ in range(N):
        action_func()
        time.sleep(1)

if __name__ == '__main__':
    repeater = ActionRepeater()
    repeat_sequence(repeater.execute_action)