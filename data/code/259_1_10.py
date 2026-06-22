def find_min_max(numbers):
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23]
    print(find_min_max(sample_values))