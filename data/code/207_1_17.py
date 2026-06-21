def find_largest_number(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"The largest number in {sample_numbers1} is: {find_largest_number(sample_numbers1)}")
    
    sample_numbers2 = [-7, -3, -8, -2]
    print(f"The largest number in {sample_numbers2} is: {find_largest_number(sample_numbers2)}")
    
    sample_numbers3 = [0, 0, 0, 0]
    print(f"The largest number in {sample_numbers3} is: {find_largest_number(sample_numbers3)}")