def find_max_element():
    numbers = {4, 8, 15, 16, 23, 42}
    max_number = max(numbers)
    return max_number

if __name__ == '__main__':
    sample_set = {7, 10, 3, 18, 29, 54}
    print(f"The largest element in the set is: {find_max_element()}")