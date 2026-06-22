def find_difference(numbers):
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = (3.5, 7.2, 1.8, 9.4)
    difference = find_difference(sample_numbers)
    print(difference)