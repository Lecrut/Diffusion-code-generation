def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_divisible_by_three = n % 3 == 0
    return {
        "value": n,
        "is_positive": is_positive,
        "is_even": is_even,
        "is_divisible_by_three": is_divisible_by_three
    }

if __name__ == '__main__':
    sample_values = [6, -3, 4, 9, 0]
    for val in sample_values:
        result = check_number(val)
        print(result)