import time

def repeat_actions():
    for _ in range(5):
        print('Action executed')
        time.sleep(2)
if __name__ == '__main__':
    repeat_actions()