REVERSE_SLICE = slice(None, None, -1)

def reverse_list(input_list):
    return input_list[REVERSE_SLICE]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)