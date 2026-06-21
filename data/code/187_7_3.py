def max_value_and_index(numbers):
    return max(enumerate(numbers), key=lambda x: x[1])

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 1]
    result = max_value_and_index(sample_numbers)
    print(f"Max value: {result[1]}, Index: {result[0]}")