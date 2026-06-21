def sort_two_floats(a, b):
    smallest = min(a, b)
    largest = max(a, b)
    return smallest, largest

if __name__ == '__main__':
    first_value = 9.8
    second_value = 3.1
    sorted_pair = sort_two_floats(first_value, second_value)
    print(sorted_pair)