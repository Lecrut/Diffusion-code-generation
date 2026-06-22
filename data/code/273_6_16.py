import time

def repeat_sequence(action_func):
    if not callable(action_func):
        raise ValueError("action_func must be a callable")
    
    for _ in range(5):
        action_func()
        time.sleep(2)

if __name__ == '__main__':
    def sample_action():
        print('Action executed')
    
    try:
        repeat_sequence(sample_action)
    except ValueError as e:
        print(e)