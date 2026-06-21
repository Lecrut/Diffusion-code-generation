sample_list = [3.14, "hello", 42, True]

def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    reversed_sample = reverse_list(sample_list)
    print(reversed_sample)