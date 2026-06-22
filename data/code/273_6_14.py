import time

def validate_delay(delay):
    if delay < 1:
        raise ValueError("Delay must be at least 1 second")

def validate_repetitions(repetitions):
    if repetitions <= 0 or not isinstance(repetitions, int):
        raise ValueError("Repetitions must be a positive integer")

def perform_action():
    print('Action executed')

def repeat_sequence(action_func=perform_action, delay=2, repetitions=5):
    validate_delay(delay)
    validate_repetitions(repetitions)
    
    for _ in range(repetitions):
        action_func()
        time.sleep(delay)

if __name__ == '__main__':
    repeat_sequence()