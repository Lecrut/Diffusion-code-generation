import time

def repeat_action(action_func):
    for _ in range(3):
        action_func()
        time.sleep(1)

if __name__ == '__main__':
    def sample_action():
        print('Action executed')

    repeat_action(sample_action)