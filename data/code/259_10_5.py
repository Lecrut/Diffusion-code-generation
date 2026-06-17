import sys
def find_min_max(data):
    if not data:
        return None, None
    smallest = data[0]
    largest = data[0]
    for x in data:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return smallest, largest
if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 67, 22]
    min_val, max_val = find_min_max(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")