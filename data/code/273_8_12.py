import time

def repeat_actions():
    for _ in range(3):
        print('Action executed')
        time.sleep(1)
if __name__ == '__main__':
    repeat_actions()