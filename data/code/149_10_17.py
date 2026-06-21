def reverse_list(input_list):
    if not isinstance(input_list, list) or not all(isinstance(x, int) for x in input_list):
        raise ValueError("Input must be a list of integers")
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        reversed_list = reverse_list(sample_list)
        print(reversed_list)
    except ValueError as e:
        print(e)