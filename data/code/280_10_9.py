def repeat_action(times):
    for _ in range(times):
        print('Action repeated')

if __name__ == '__main__':
    times_to_repeat = 5
    if times_to_repeat < 1:
        raise ValueError("Number of repetitions must be at least 1")
    
    repeat_action(times_to_repeat)