def repeat_pattern(base_list, target_length):
    return base_list * (target_length // len(base_list)) + base_list[:target_length % len(base_list)]

if __name__ == '__main__':
    sample_base_list = [1, 2, 3]
    sample_target_length = 7
    result = repeat_pattern(sample_base_list, sample_target_length)
    print(result)