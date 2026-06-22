def find_the_middle_value_among_three_summary(a, b, c):
    values = [a, b, c]
    if len(values) != 3:
        raise ValueError("Exactly three values must be provided")
    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError("All values must be numbers")
    sorted_values = sorted(values)
    return sorted_values[1]

if __name__ == '__main__':
    a = 10
    b = 5
    c = 20
    try:
        middle_value = find_the_middle_value_among_three_summary(a, b, c)
        print(middle_value)
    except (ValueError, TypeError) as e:
        print(e)