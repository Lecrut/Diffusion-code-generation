def find_max_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9]
    print(find_max_element(sample_values))