import time

REPEAT_COUNT = 5
DELAY_SECONDS = 1

def repeat_action(action_string):
    for _ in range(REPEAT_COUNT):
        print(action_string)
        time.sleep(DELAY_SECONDS)

if __name__ == '__main__':
    action = "Hello World"
    repeat_action(action)