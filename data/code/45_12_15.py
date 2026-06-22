def find_minimum(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_data = [3.14, 2.71, 9.81, 0.57, -1.25, 4.66]
    result = find_minimum(sample_data)
    print(result)