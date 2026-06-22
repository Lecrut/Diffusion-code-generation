import time

def repeat_sequence():
    for _ in range(10):
        print('Action performed')
        time.sleep(0.5)
if __name__ == '__main__':
    repeat_sequence()