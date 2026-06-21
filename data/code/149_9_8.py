def reverse_mixed_list(mixed_list):
    return mixed_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 'a', 3.14, True, None]
    reversed_list = reverse_mixed_list(sample_list)
    print(reversed_list)