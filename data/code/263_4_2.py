def find_largest_and_smallest(data):
    if not data:
        return None, None
    largest = data[0]
    smallest = data[0]
    for number in data[1:]:
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number
    return largest, smallest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    largest_val, smallest_val = find_largest_and_smallest(sample_list)
    print(f"List: {sample_list}")
    print(f"Largest value: {largest_val}")
    print(f"Smallest value: {smallest_val}")
    sample_list_2 = [-10, 5, -20, 3]
    largest_val_2, smallest_val_2 = find_largest_and_smallest(sample_list_2)
    print(f"\nList: {sample_list_2}")
    print(f"Largest value: {largest_val_2}")
    print(f"Smallest value: {smallest_val_2}")
    sample_list_3 = [7]
    largest_val_3, smallest_val_3 = find_largest_and_smallest(sample_list_3)
    print(f"\nList: {sample_list_3}")
    print(f"Largest value: {largest_val_3}")
    print(f"Smallest value: {smallest_val_3}")
    sample_list_4 = []
    largest_val_4, smallest_val_4 = find_largest_and_smallest(sample_list_4)
    print(f"\nList: {sample_list_4}")
    print(f"Largest value: {largest_val_4}")
    print(f"Smallest value: {smallest_val_4}")