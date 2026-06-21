def reverse_list(mixed_list):
    return mixed_list[::-1]

if __name__ == '__main__':
    sample = [1, 'a', 3.14, True, None]
    reversed_sample = reverse_list(sample)
    print(reversed_sample)