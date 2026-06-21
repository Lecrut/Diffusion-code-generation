def sort_mixed_numbers(numbers):
    return sorted(numbers, key=float)

if __name__ == '__main__':
    sample_values = [3.5, 2, 4.8, '1', 0.9]
    print(sort_mixed_numbers(sample_values))