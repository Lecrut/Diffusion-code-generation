import time

def perform_action():
    print('Action executed')

def repeat_sequence(action_func):
    actions = {1: action_func}
    for _ in range(3):
        actions[1]()
        time.sleep(1)

if __name__ == '__main__':
    repeat_sequence(perform_action)