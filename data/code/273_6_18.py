import time
DELAY_SECONDS = 2
REPETITIONS = 5

def perform_action():
    print('Action performed')

def repeat_sequence(action_func):
    for _ in range(REPETITIONS):
        action_func()
        time.sleep(DELAY_SECONDS)
if __name__ == '__main__':
    sample_action = perform_action
    repeat_sequence(sample_action)