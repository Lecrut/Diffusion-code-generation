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
    sample_list = [34, 12, 56, 89, 23, 77]
    minimum, maximum = find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"The smallest element is: {minimum}")
    print(f"The largest element is: {maximum}")
    sample_list_2 = [-10, 5, 0, -20, 3]
    minimum_2, maximum_2 = find_min_max(sample_list_2)
    print(f"\nThe list is: {sample_list_2}")
    print(f"The smallest element is: {minimum_2}")
    print(f"The largest element is: {maximum_2}")
    sample_list_3 = [42]
    minimum_3, maximum_3 = find_min_max(sample_list_3)
    print(f"\nThe list is: {sample_list_3}")
    print(f"The smallest element is: {minimum_3}")
    print(f"The largest element is: {maximum_3}")
    sample_list_4 = []
    minimum_4, maximum_4 = find_min_max(sample_list_4)
    print(f"\nThe list is: {sample_list_4}")
    print(f"The smallest element is: {minimum_4}")
    print(f"The largest element is: {maximum_4}")