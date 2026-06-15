def find_min_max(data):
    if not data:
        return None, None                              
    current_min = data[0]
    current_max = data[0]
    for element in data[1:]:
        if element < current_min:
            current_min = element
        if element > current_max:
            current_max = element
    return current_min, current_max
if __name__ == '__main__':
    sample_list = [15, 3, 88, 42, 9, 71]
    minimum, maximum = find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"The minimum element is: {minimum}")
    print(f"The maximum element is: {maximum}")
    sample_tuple = (100, 50, 200, 10, 150)
    minimum_t, maximum_t = find_min_max(sample_tuple)
    print(f"\nThe tuple is: {sample_tuple}")
    print(f"The minimum element is: {minimum_t}")
    print(f"The maximum element is: {maximum_t}")
    empty_list = []
    minimum_e, maximum_e = find_min_max(empty_list)
    print(f"\nThe empty list is: {empty_list}")
    print(f"The minimum element is: {minimum_e}")
    print(f"The maximum element is: {maximum_e}")