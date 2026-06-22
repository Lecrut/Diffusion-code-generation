def find_min_max_integers(integer_list):
    if not integer_list:
        raise ValueError("Input list cannot be empty")
    
    min_value = max_value = integer_list[0]
    
    for number in integer_list[1:]:
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number
    
    return min_value, max_value

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, 90]
    minimum, maximum = find_min_max_integers(sample_list)
    print(f"List: {sample_list}")
    print(f"Minimum integer value: {minimum}")
    print(f"Maximum integer value: {maximum}")