DEFAULT_SAMPLE_LIST = [1, 2, 3, 4, 5]

def reverse_list(input_list):
    return input_list[::-1]
if __name__ == '__main__':
    sample_list = DEFAULT_SAMPLE_LIST
    reversed_list = reverse_list(sample_list)
    print(reversed_list)