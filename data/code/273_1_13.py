def repeat_action(action, times=10):
    if not isinstance(times, int) or times < 1:
        raise ValueError("Times must be a positive integer")
    
    for _ in range(times):
        action()

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")

    repeat_action(sample_action)