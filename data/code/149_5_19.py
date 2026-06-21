def validate_input(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, (int, float)) for item in lst):
        raise ValueError("All elements of the list must be numbers")

def reverse_list(lst):
    validate_input(lst)
    return lst[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    print(reverse_list(sample))