def find_max_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 7.8, 4.9]
    print(find_max_element(sample_numbers))