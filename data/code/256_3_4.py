def find_range(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_set = {5, 3, 9, 1, 7}
    print(find_range(sample_set))