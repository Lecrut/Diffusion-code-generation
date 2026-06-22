def find_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_set = {3, 5, 1, 2, 4}
    print(find_range(sample_set))