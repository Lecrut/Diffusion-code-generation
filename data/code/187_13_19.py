def find_highest_number(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

if __name__ == '__main__':
    sample_numbers = [15, 27, 4, 98, 63]
    print(find_highest_number(sample_numbers))