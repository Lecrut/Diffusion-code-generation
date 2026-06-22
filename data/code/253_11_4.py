def find_the_middle_value_among_three_format_results(a, b, c):
    try:
        numbers = sorted([a, b, c])
        middle_index = len(numbers) // 2
        middle_value = numbers[middle_index]
        return f'The middle value among {a}, {b}, and {c} is {middle_value}.'
    except TypeError as e:
        return 'Invalid input: All arguments must be numbers.'
if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 4))
    print(find_the_middle_value_among_three_format_results(7, 7, 7))
    print(find_the_middle_value_among_three_format_results('a', 3, 4))