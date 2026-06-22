def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers)

if __name__ == "__main__":
    sample_list = [5, 2, 9, 1, 7]
    result = find_minimum(sample_list)
    print(result)