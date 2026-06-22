def find_the_middle_value_among_three_format_results(a, b, c):
    numbers = sorted([a, b, c])
    return f"The middle value among {a}, {b}, and {c} is {numbers[1]}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 4))