SAMPLE_LIST = [1, 2, 3, 4, 5]

def reverse_list(input_list):
    return input_list[::-1]
if __name__ == '__main__':
    reversed_sample = reverse_list(SAMPLE_LIST)
    print(reversed_sample)