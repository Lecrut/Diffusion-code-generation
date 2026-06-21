def find_highest_number(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

if __name__ == '__main__':
    sample_numbers = [12, 45, 78, 34, 90, 67]
    print(find_highest_number(sample_numbers))