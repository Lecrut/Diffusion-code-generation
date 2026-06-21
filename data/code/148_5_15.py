MAX_VALUE = float('-inf')

def find_largest(data):
    if not data:
        return None
    largest = MAX_VALUE
    for element in data:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    largest_element = find_largest(sample_list)
    print(largest_element)