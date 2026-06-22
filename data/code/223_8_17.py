def find_largest_number(numbers):
    numbers.sort(reverse=True)
    return numbers[0]

if __name__ == '__main__':
    sample_numbers = [3, 5, 2, 8, 1]
    print(find_largest_number(sample_numbers))