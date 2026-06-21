def is_valid_list(lst):
    return isinstance(lst, list) and all(isinstance(item, (int, float)) for item in lst)

def reverse_list(lst):
    if not is_valid_list(lst):
        raise ValueError("Input must be a list of numbers")
    return lst[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    print(reverse_list(sample))