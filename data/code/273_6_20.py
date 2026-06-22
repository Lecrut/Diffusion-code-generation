import time

def repeat_action(action, delay=2, repetitions=5):
    for _ in range(repetitions):
        action()
        time.sleep(delay)

if __name__ == '__main__':
    sample_action = lambda: print('Action executed')
    repeat_action(sample_action)