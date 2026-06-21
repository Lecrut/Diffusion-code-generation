MAX_INT = 2**31 - 1

def find_highest_number(numbers):
    highest = MAX_INT
    for num in numbers:
        if num > highest:
            highest = num
    return highest

if __name__ == '__main__':
    sample_numbers = [4, 7, 1, 8, 2, 9]
    print(find_highest_number(sample_numbers))