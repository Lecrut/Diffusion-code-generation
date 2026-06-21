HIGHEST_NUMBER = float('-inf')

def find_highest_number(numbers):
    highest = HIGHEST_NUMBER
    for num in numbers:
        if num > highest:
            highest = num
    return highest

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(find_highest_number(sample_numbers))