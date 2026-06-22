import time
ACTION_DELAY = 1

def execute_action():
    print('Action executed')

def repeat_sequence(action_func):
    for _ in range(3):
        action_func()
        time.sleep(ACTION_DELAY)
if __name__ == '__main__':
    repeat_sequence(execute_action)