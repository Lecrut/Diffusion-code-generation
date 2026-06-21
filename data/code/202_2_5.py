def find_greatest_number(numbers):
    if not numbers:
        return None
    greatest = numbers[0]
    for num in numbers:
        if num > greatest:
            greatest = num
    return greatest

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4, 8, 7, 6]
    print(find_greatest_number(sample_numbers))