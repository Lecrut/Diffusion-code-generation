import time

def repeat_action(action_string: str) -> None:
    for _ in range(5):
        print(action_string)
        time.sleep(1)

if __name__ == '__main__':
    action = "Hello World"
    repeat_action(action)