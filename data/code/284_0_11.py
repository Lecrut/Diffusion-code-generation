REVERSED_LIST_SLICE = slice(None, None, -1)

def reverse_list(input_list):
    return input_list[REVERSED_LIST_SLICE]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reversed_sample = reverse_list(sample_values)
    print(reversed_sample)