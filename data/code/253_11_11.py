def find_the_middle_value_among_three_format_results(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    middle_index = len(numbers) // 2
    middle_value = numbers[middle_index]
    return f"The middle value among {a}, {b}, and {c} is {middle_value}."

if __name__ == '__main__':
    result1 = find_the_middle_value_among_three_format_results(5, 3, 4)
    result2 = find_the_middle_value_among_three_format_results(7, 7, 7)
    print(result1)
    print(result2)