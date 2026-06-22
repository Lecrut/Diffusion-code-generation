import time

def repeat_action():
    print("Action executed")

if __name__ == '__main__':
    for _ in range(3):
        repeat_action()
        time.sleep(1)