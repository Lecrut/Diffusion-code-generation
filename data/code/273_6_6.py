import time

def repeat_sequence():
    for _ in range(5):
        print('Performing action...')
        time.sleep(2)
if __name__ == '__main__':
    repeat_sequence()