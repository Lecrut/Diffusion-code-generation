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
    large_list = [45, 12, 89, 3, 67, 22, 91, 50, 1]
    print("Original List:", large_list)
    min_val, max_val = find_min_max_manually(large_list)
    print("Manually calculated Smallest element:", min_val)
    print("Manually calculated Largest element:", max_val)