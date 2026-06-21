def reverse_list(mixed_list):
    return mixed_list[::-1]

if __name__ == '__main__':
    sample = [42, "hello", 3.14, True]
    print(reverse_list(sample))