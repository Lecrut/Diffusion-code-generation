import time

def repeat_sequence():
    for _ in range(3):
        print("Action")
        time.sleep(1)

if __name__ == '__main__':
    repeat_sequence()