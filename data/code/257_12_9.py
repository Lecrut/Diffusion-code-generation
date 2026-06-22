def find_difference(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = (3.5, 2.1, 4.8, 1.9)
    print(find_difference(sample_values))