import time

def repeat_action(action_func):
    for _ in range(10):
        action_func()
        time.sleep(0.5)

if __name__ == '__main__':
    sample_action = lambda: print("Action executed")
    repeat_action(sample_action)