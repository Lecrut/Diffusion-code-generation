import sys
def find_min_max(data):
    if not data:
        return None, None
    smallest = data[0]
    largest = data[0]
    for number in data:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return smallest, largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    min_val, max_val = find_min_max(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")