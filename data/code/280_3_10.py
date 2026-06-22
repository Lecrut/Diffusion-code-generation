import time

def repeat_action(action_string: str, num_times: int):
    for _ in range(num_times):
        print(action_string)
        time.sleep(1)

if __name__ == '__main__':
    action = "Repeat Me"
    count = 5
    repeat_action(action, count)