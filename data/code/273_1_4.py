def repeat_action(action, times=10):
    if not isinstance(times, int) or times < 1:
        raise ValueError("Times must be a positive integer")
    
    count = 0
    while count < times:
        action()
        count += 1

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action)