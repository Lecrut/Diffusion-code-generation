import time

def perform_action():
    print("Action")

def validate_and_repeat(action_func):
    if not callable(action_func):
        raise ValueError("Provided action is not callable")
    for _ in range(10):
        action_func()
        time.sleep(0.5)

if __name__ == '__main__':
    sample_action = perform_action
    validate_and_repeat(sample_action)