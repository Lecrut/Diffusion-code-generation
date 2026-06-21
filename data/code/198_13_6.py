def get_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [15, 3, 8, 22, 1]
    minimum_value = get_minimum(sample_list)
    print(minimum_value)