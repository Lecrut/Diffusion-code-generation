import time

REPEAT_COUNT = 3
DELAY_SECONDS = 1

def execute_sequence():
    print('Action executed')

def repeat_sequence(action_func):
    for _ in range(REPEAT_COUNT):
        action_func()
        time.sleep(DELAY_SECONDS)

if __name__ == '__main__':
    repeat_sequence(execute_sequence)