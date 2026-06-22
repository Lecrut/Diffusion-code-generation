import time

def perform_action():
    print("Action executed")

def repeat_sequence(action_func):
    for _ in range(10):
        action_func()
        time.sleep(0.5)

if __name__ == '__main__':
    sample_action = perform_action
    repeat_sequence(sample_action)