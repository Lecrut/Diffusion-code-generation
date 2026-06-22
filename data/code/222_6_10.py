def find_min(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min(sample_list))