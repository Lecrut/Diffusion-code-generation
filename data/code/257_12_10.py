def find_max_min_difference(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    print(find_max_min_difference(sample_values))