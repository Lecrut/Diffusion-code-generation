def find_the_middle_value_among_three_summary(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    sorted_values = sorted([a, b, c])
    return sorted_values[1]

if __name__ == '__main__':
    try:
        print(find_the_middle_value_among_three_summary(3, 1, 2))
        print(find_the_middle_value_among_three_summary(10, 5, 20))
        print(find_the_middle_value_among_three_summary(10, 25, 15))
    except ValueError as e:
        print(e)