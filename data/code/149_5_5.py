def validate_input(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst

def reverse_list(lst):
    validated_lst = validate_input(lst)
    return validated_lst[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    print(reverse_list(sample))