import time

def repeat_action():
    for _ in range(5):
        print("Action executed")
        time.sleep(1)

if __name__ == '__main__':
    repeat_action()