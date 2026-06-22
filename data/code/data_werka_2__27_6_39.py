def validate_input(input_list):
    if not isinstance(input_list, (list, tuple)):
        raise ValueError("Input must be a list or a tuple.")
    for num in input_list:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers.")

def are_sums_different(list1, list2):
    validate_input(list1)
    validate_input(list2)
    
    sum1 = sum(list1)
    sum2 = sum(list2)
    
    return sum1 != sum2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [5, 4, 3, 2, 10]
    result = are_sums_different(sample_list1, sample_list2)
    print(result)