def find_largest_number(numbers):
    return sorted(numbers, reverse=True)[0]

if __name__ == '__main__':
    sample_numbers = [34, 12, 98, 56, 78]
    print(find_largest_number(sample_numbers))