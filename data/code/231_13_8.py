def repeat_pattern(base_list, target_length):
    return base_list * ((target_length // len(base_list)) + 1)[:target_length]

if __name__ == '__main__':
    sample_base = ['a', 'b', 'c']
    sample_length = 7
    print(repeat_pattern(sample_base, sample_length))