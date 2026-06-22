def print_unique_elements(lst):
    if not all(isinstance(item, int) for item in lst):
        raise ValueError("All elements in the list must be integers.")
    
    unique_elements = set(lst)
    for element in unique_elements:
        print(element)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print_unique_elements(sample_list)
    except ValueError as e:
        print(e)