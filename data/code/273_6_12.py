import time

def repeat_sequence(action_func):
    try:
        if not callable(action_func):
            raise ValueError("action_func must be callable")
        for _ in range(5):
            action_func()
            time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample_action = lambda: print('Action executed')
    repeat_sequence(sample_action)