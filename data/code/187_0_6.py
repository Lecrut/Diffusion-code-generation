def find_max_element(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 35]
    try:
        largest = find_max_element(sample_list)
        print(largest)
    except ValueError as e:
        print(e)