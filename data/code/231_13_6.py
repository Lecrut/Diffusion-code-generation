def repeat_pattern(base_list, target_length):
    return [base_list[i % len(base_list)] for i in range(target_length)]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c']
    desired_length = 8
    result = repeat_pattern(sample_list, desired_length)
    print(result)