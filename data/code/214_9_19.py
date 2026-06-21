def find_smallest(numbers):
    if not numbers:
        raise ValueError("The input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5]
    print(find_smallest(sample_values))