def find_max_element():
    numbers = {4, 8, 15, 16, 23, 42}
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_set = {4, 8, 15, 16, 23, 42}
    print(f"The maximum element in the set is: {find_max_element()}")