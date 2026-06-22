def repeat_pattern(base_list, target_length):
    return [base_list[i % len(base_list)] for i in range(target_length)]

if __name__ == '__main__':
    sample_base = ['a', 'b', 'c']
    sample_length = 10
    print(repeat_pattern(sample_base, sample_length))