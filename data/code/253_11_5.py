def find_the_middle_value_among_three_format_results(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    middle_index = len(numbers) // 2
    return f"The middle value among {a}, {b}, and {c} is {numbers[middle_index]}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(10, 5, 20))
    print(find_the_middle_value_among_three_format_results(7, 7, 7))
    print(find_the_middle_value_among_three_format_results(3, 9, 6))