def find_highest_number(numbers):
    highest = None
    for num in numbers:
        if highest is None or num > highest:
            highest = num
    return highest

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_highest_number(sample_numbers))