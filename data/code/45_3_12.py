def get_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers)

if __name__ == "__main__":
    sample_data = [5, 2, 9, 1, 7]
    result = get_minimum(sample_data)
    print(result)