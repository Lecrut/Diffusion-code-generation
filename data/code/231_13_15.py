def repeat_pattern(base_list, target_length):
    return [base_list[i % len(base_list)] for i in range(target_length)]

if __name__ == '__main__':
    base_list = ['a', 'b', 'c']
    target_length = 10
    result = repeat_pattern(base_list, target_length)
    print(result)