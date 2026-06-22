def repeat_pattern(base_list, target_length):
    return base_list * (target_length // len(base_list)) + base_list[:target_length % len(base_list)]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c']
    length = 10
    print(repeat_pattern(sample_list, length))