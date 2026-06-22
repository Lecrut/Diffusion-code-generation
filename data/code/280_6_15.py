def repeat_action(times, break_on):
    for i in range(1, times + 1):
        if i == break_on:
            break
        print(f"Action {i}")

if __name__ == '__main__':
    sample_times = 5
    sample_break_on = 3
    try:
        repeat_action(sample_times, sample_break_on)
    except Exception as e:
        print(f"Error: {e}")