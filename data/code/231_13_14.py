def repeat_pattern(base_list, target_length):
    if not base_list:
        return []
    pattern = []
    for i in range(target_length):
        pattern.append(base_list[i % len(base_list)])
    return pattern

if __name__ == '__main__':
    sample_base_list = ['a', 'b', 'c']
    sample_target_length = 7
    result = repeat_pattern(sample_base_list, sample_target_length)
    print(result)