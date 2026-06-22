def find_max_number(numbers):
    if not numbers:
        raise ValueError("Input string cannot be empty")
    number_list = list(map(int, numbers.split()))
    max_value = number_list[0]
    for number in number_list[1:]:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_string = "3 45 2 9 78"
    try:
        maximum = find_max_number(sample_string)
        print(maximum)
    except ValueError as e:
        print(e)