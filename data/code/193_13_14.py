def validate_input(lst):
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("All elements must be numbers")

def sum_elements(lst):
    validate_input(lst)
    return sum(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(sum_elements(sample_list))