def find_the_middle_value_among_three_format_results(a, b, c):
    numbers = sorted([a, b, c])
    return f"The middle value among {numbers[0]}, {numbers[1]}, and {numbers[2]} is {numbers[1]}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 4))