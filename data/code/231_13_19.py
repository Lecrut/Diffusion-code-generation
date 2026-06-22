def repeat_pattern(base_list, target_length):
    return base_list * (target_length // len(base_list)) + base_list[:target_length % len(base_list)]

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    length = 8
    result = repeat_pattern(sample_list, length)
    print(result)