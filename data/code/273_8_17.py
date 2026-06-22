import time

def execute_action():
    print("Action executed")

def validate_repetitions(N):
    if not isinstance(N, int) or N <= 0:
        raise ValueError("Number of repetitions must be a positive integer")

def repeat_sequence(action_func, N=3):
    validate_repetitions(N)
    for _ in range(N):
        action_func()
        time.sleep(1)

if __name__ == '__main__':
    repeat_sequence(execute_action)