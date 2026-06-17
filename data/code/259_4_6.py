def find_min_max_manually(data):
    if not data:
        return None, None
    smallest = data[0]
    largest = data[0]
    for number in data[1:]:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return smallest, largest
if __name__ == '__main__':
    large_list = [45, 12, 89, 3, 67, 22, 91, 5, 78, 33]
    print("Original List:", large_list)
    smallest_val, largest_val = find_min_max_manually(large_list)
    print("Manually calculated Smallest element:", smallest_val)
    print("Manually calculated Largest element:", largest_val)