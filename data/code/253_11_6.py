def find_the_middle_value_among_three_format_results(a, b, c):
    middle = sorted([a, b, c])[1]
    return f"The middle value among {a}, {b}, and {c} is {middle}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 8))