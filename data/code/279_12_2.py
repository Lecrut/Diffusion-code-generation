def find_even_numbers(start, end):
    result = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            result.append(number)
    return result
if __name__ == '__main__':
    start_value = 1
    end_value = 20
    even_list = find_even_numbers(start_value, end_value)
    print(even_list)