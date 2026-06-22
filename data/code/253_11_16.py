def find_the_middle_value_among_three_format_results(a, b, c):
    return f"The middle value among {a}, {b}, and {c} is {'middle' if a == b or b == c or a == c else 'not determined'}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(1, 2, 3))
    print(find_the_middle_value_among_three_format_results(5, 5, 7))
    print(find_the_middle_value_among_three_format_results(8, 6, 6))