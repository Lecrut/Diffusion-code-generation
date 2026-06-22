def find_min_max(numbers):
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 0.7]
    print(find_min_max(sample_values))