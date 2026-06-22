import time

def repeat_action(action_func):
    if not callable(action_func):
        raise ValueError("action_func must be a callable")
    for _ in range(3):
        action_func()
        time.sleep(1)

if __name__ == '__main__':
    def sample_action():
        print('Action executed')

    try:
        repeat_action(sample_action)
    except ValueError as e:
        print(e)