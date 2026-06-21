def validate_input(lst):
    if not isinstance(lst, list) or not all(isinstance(item, (int, float)) for item in lst):
        raise ValueError("Input must be a list of numbers")

def reverse_list(lst):
    validate_input(lst)
    return lst[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)