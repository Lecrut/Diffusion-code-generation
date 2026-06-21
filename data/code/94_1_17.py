def check_any_true(iterable):
    truth_counter = 0
    for element in iterable:
        if element:
            truth_counter += 1
            break
    return truth_counter > 0

if __name__ == '__main__':
    sample_data = [False, False, False, False, False]
    result_value = check_any_true(sample_data)
    print(result_value)