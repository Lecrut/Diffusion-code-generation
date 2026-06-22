import time

def execute_action():
    print("Action executed")

def validate_repetitions(count):
    if count < 1:
        raise ValueError("Repetition count must be at least 1")

def repeat_sequence(action, repetitions=3):
    validate_repetitions(repetitions)
    for _ in range(repetitions):
        action()
        time.sleep(1)

if __name__ == '__main__':
    repeat_sequence(execute_action)