def find_the_middle_value_among_three_format_results(a, b, c):
    numbers = [a, b, c]
    if len(numbers) != 3:
        raise ValueError("Exactly three numbers are required.")
    sorted_numbers = sorted(numbers)
    middle_index = len(sorted_numbers) // 2
    return f"The middle value among {a}, {b}, and {c} is {sorted_numbers[middle_index]}."

if __name__ == '__main__':
    print(find_the_middle_value_among_three_format_results(5, 3, 4))
    print(find_the_middle_value_among_three_format_results(7, 7, 7))