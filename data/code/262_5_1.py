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
    print(f"List: {sample_list}")
    print(f"Smallest element: {minimum}")
    print(f"Largest element: {maximum}")