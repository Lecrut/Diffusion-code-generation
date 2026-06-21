def min_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0]
    print(min_value(sample_values))