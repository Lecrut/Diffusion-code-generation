def max_value(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numeric")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    print(max_value(sample_list))