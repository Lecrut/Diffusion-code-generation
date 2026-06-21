def find_largest_integer(array):
    if not array:
        raise ValueError("Array cannot be empty")
    
    max_value = array[0]
    for num in array:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == '__main__':
    sample_array = [100, 200, 50, 300, 75]
    try:
        largest_integer = find_largest_integer(sample_array)
        print(largest_integer)
    except ValueError as e:
        print(e)