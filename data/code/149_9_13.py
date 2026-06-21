def reverse_mixed_list(mixed_list):
    return mixed_list[::-1]

if __name__ == '__main__':
    sample = [42, "world", 2.718, False, None]
    reversed_sample = reverse_mixed_list(sample)
    print(reversed_sample)