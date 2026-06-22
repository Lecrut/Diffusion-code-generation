def find_the_middle_value_among_three_format_results(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    middle_index = len(numbers) // 2
    middle_value = numbers[middle_index]
    return f"The middle value among {a}, {b}, and {c} is {middle_value}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 4))