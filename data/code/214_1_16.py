def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    print(f"Minimum of {sample_list}: {find_minimum(sample_list)}")