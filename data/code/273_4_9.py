import time

def execute_action():
    print("Action executed")

def validate_input(action_func):
    if not callable(action_func):
        raise ValueError("Provided action is not callable")

def repeat_sequence(action_func, delay=0.5, repetitions=10):
    validate_input(action_func)
    for _ in range(repetitions):
        action_func()
        time.sleep(delay)

if __name__ == '__main__':
    sample_action = execute_action
    repeat_sequence(sample_action)