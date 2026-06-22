import time

def repeat_sequence(action_func):
    if not callable(action_func):
        raise ValueError("The action_func must be a callable function.")
    
    for _ in range(10):
        action_func()
        time.sleep(0.5)

if __name__ == '__main__':
    def sample_action():
        print("Action executed")
    
    repeat_sequence(sample_action)