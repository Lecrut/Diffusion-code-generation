def find_range(numbers):
    if len(numbers) < 2:
        return None
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_range(sample_values))