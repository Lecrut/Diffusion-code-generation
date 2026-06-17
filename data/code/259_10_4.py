import sys
def find_min_max(data):
    if not data:
        return None, None
    smallest = data[0]
    largest = data[0]
    for num in data[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest
if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    min_val, max_val = find_min_max(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")