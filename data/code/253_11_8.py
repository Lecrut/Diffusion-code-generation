def find_the_middle_value_among_three_format_results(a, b, c):
    return f"The middle value among {a}, {b}, and {c} is {'middle' if a == b == c else sorted([a, b, c])[1]}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(3, 1, 2))
    print(find_the_middle_value_among_three_format_results(5, 5, 5))