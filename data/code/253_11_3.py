def find_the_middle_value_among_three_format_results(a, b, c):
    return f"The middle value among {a}, {b}, and {c} is {'middle' if a < b < c or a > b > c else 'not middle'}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 4))