import time

def repeat_sequence(action):
    for _ in range(3):
        action()
        time.sleep(1)

if __name__ == '__main__':
    def sample_action():
        print('Action executed')

    repeat_sequence(sample_action)