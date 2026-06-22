def sum_sequence(numbers):
    try:
        return sum(numbers)
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = sum_sequence(sample_numbers)
    if result is not None:
        print(result)