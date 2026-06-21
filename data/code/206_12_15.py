def find_minimum(values):
    if not values:
        raise ValueError("List cannot be empty")
    minimum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
    return minimum

if __name__ == '__main__':
    sample_list_1 = [15, 3, 7, 29, -4, 8]
    min1 = find_minimum(sample_list_1)
    print(f"Minimum of {sample_list_1}: {min1}")
    
    sample_list_2 = [0, 0, 0, 0, 0]
    min2 = find_minimum(sample_list_2)
    print(f"Minimum of {sample_list_2}: {min2}")
    
    sample_list_3 = [-5, -10, -3, -8, -1]
    min3 = find_minimum(sample_list_3)
    print(f"Minimum of {sample_list_3}: {min3}")