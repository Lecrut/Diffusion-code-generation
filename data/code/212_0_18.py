def find_min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_min_max(sample_values))