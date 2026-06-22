def find_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_set = {3, 1, 4, 1, 5, 9, 2}
    print(find_range(sample_set))