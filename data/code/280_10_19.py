def repeat_action(action, times):
    if not callable(action) or not isinstance(times, int) or times < 0:
        raise ValueError("Invalid input: action must be callable and times must be a non-negative integer")
    
    for _ in range(times):
        action()

if __name__ == '__main__':
    def sample_action():
        print('Repeat an action five times now')

    repeat_action(sample_action, 5)