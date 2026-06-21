def find_largest_element(data):
    if not data:
        raise ValueError("Cannot find maximum of an empty list.")
    
    max_value = data[0]
    for value in data[1:]:
        if value > max_value:
            max_value = value
    
    return max_value

if __name__ == '__main__':
    sample_list_one = [15, 8, 32, 7, 41, 19]
    try:
        largest_element = find_largest_element(sample_list_one)
        print(f"The largest element in {sample_list_one} is: {largest_element}")
    except ValueError as e:
        print(f"Error for sample list one: {e}")

    sample_list_two = [0, -10, 25, 4, 1]
    try:
        largest_element = find_largest_element(sample_list_two)
        print(f"The largest element in {sample_list_two} is: {largest_element}")
    except ValueError as e:
        print(f"Error for sample list two: {e}")