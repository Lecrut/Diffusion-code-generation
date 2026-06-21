def find_highest_number(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

if __name__ == '__main__':
    sample_numbers = [7, 2, 9, 3, 5]
    print(find_highest_number(sample_numbers))