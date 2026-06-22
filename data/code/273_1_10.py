def repeat_action(action, times):
    if not isinstance(times, int) or times < 0:
        raise ValueError("Number of repetitions must be a non-negative integer")
    
    count = 0
    while count < times:
        action()
        count += 1

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action, 10)