def find_min_max(data):
    if not data:
        return None, None
    smallest = data[0]
    largest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
        if element > largest:
            largest = element
    return smallest, largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    minimum, maximum = find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"The smallest element is: {minimum}")
    print(f"The largest element is: {maximum}")
    sample_list_2 = [-10, 5, 0, -20, 100]
    minimum_2, maximum_2 = find_min_max(sample_list_2)
    print(f"\nThe list is: {sample_list_2}")
    print(f"The smallest element is: {minimum_2}")
    print(f"The largest element is: {maximum_2}")
    empty_list = []
    minimum_3, maximum_3 = find_min_max(empty_list)
    print(f"\nThe list is: {empty_list}")
    print(f"The smallest element is: {minimum_3}")
    print(f"The largest element is: {maximum_3}")