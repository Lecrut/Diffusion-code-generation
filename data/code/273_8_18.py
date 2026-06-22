import time

def execute_action():
    print("Action performed")

def repeat_sequence(action_func):
    for _ in range(3):
        action_func()
        time.sleep(1)

if __name__ == '__main__':
    sample_action = execute_action
    repeat_sequence(sample_action)