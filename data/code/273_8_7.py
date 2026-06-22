import time

def execute_action():
    print("Action executed")

def repeat_sequence(action_func):
    for _ in range(3):
        action_func()
        time.sleep(1)

if __name__ == '__main__':
    action = execute_action
    repeat_sequence(action)