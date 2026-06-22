def find_min(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_list = [34, -50, 42, 14, 55, -10]
    result = find_min(sample_list)
    print(result)