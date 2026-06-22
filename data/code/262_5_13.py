def find_min_max(data):
    if not data:
        return None, None
    smallest = largest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
        elif element > largest:
            largest = element
    return smallest, largest

if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 3, 77, 21]
    minimum, maximum = find_min_max(sample_list)
    print(f"The list is: {sample_list}")
    print(f"The smallest element is: {minimum}")
    print(f"The largest element is: {maximum}")