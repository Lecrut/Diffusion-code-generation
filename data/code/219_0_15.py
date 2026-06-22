def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    try:
        print(f"Max of {sample_list}: {find_max(sample_list)}")
    except ValueError as e:
        print(e)