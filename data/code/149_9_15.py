def reverse_mixed_list(mixed_list):
    return mixed_list[::-1]

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, True, None]
    print(reverse_mixed_list(sample_list))