def repeat_action(max_iterations, break_value):
    count = 0
    while count < max_iterations:
        if count == break_value:
            break
        print(f"Action {count + 1}")
        count += 1

if __name__ == '__main__':
    sample_max_iterations = 5
    sample_break_value = 3
    repeat_action(sample_max_iterations, sample_break_value)