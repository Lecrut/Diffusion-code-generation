def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = find_minimum(sample_list)
    print(result)