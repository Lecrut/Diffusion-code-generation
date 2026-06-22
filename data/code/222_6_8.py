def find_min(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min(sample_list))