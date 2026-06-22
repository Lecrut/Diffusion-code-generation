def find_min(numbers):
    if not numbers:
        raise ValueError("The input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9]
    print(find_min(sample_list))