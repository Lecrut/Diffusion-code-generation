def find_min_max(numbers):
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = [34, 56, 23, 89, 12, 78]
    print(find_min_max(sample_values))