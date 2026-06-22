import time

DELAY_SECONDS = 1
REPEAT_COUNT = 5

def repeat_action(action_string):
    result = ""
    for _ in range(REPEAT_COUNT):
        result += action_string + "\n"
        time.sleep(DELAY_SECONDS)
    return result.strip()

if __name__ == '__main__':
    action = "Hello World"
    output = repeat_action(action)
    print(output)