def find_min(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 9.8, 0.4, 5.6]
    empty_data = []
    print(find_min(sample_data))
    try:
        find_min(empty_data)
    except ValueError as e:
        print(e)