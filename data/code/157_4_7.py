def find_smallest_number(numbers):
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("All elements in the list must be numeric")
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [-5, 3, -2, 7, 0]
    print(find_smallest_number(sample_numbers))