def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_list = [3.14, 1.41, 2.72, 0.58, 1.62]
    result = find_minimum(sample_list)
    print(result)