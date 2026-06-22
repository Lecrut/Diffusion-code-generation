def repeat_pattern(base_list, target_length):
    if not base_list:
        return []
    pattern = []
    for i in range(target_length):
        pattern.append(base_list[i % len(base_list)])
    return pattern

if __name__ == '__main__':
    base_list = ['a', 'b', 'c']
    target_length = 7
    result = repeat_pattern(base_list, target_length)
    print(result)