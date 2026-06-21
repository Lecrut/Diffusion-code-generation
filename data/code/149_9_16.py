MIXED_LIST = [1, "hello", 3.14, True, None]

def reverse_list(mixed_list):
    return mixed_list[::-1]

if __name__ == '__main__':
    reversed_sample = reverse_list(MIXED_LIST)
    print(reversed_sample)