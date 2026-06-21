def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")

def reverse_using_iter(lst):
    validate_input(lst)
    return list(reversed(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_using_iter(sample_list)
    print(reversed_list)