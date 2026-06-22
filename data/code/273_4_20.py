import time

def repeat_sequence(action_func):
    for _ in range(10):
        action_func()
        time.sleep(0.5)

def sample_action():
    print("Action performed")

if __name__ == '__main__':
    repeat_sequence(sample_action)