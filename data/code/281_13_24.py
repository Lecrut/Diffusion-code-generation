def sum_of_integers():
    numbers = [-10, -5, 0, 5, 10, 15]
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == '__main__':
    sample_numbers = [3, 7, -2, 8, -4, 6]
    result = sum_of_integers()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")
    print(f"Sum of ({sample_numbers}): {sum(sample_numbers)}")