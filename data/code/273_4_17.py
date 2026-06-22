import time

def execute_action():
    print("Action executed")

def repeat_sequence(action_func):
    if not callable(action_func):
        raise ValueError("The provided action must be callable")
    
    for _ in range(10):
        action_func()
        time.sleep(0.5)

if __name__ == '__main__':
    sample_action = execute_action
    repeat_sequence(sample_action)