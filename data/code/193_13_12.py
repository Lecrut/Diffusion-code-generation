def validate_list(lst):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input must be a list of numbers")

def sum_elements(lst):
    validate_list(lst)
    return sum(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(sum_elements(sample_list))