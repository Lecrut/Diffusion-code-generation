def find_even_numbers(start, end):
    result = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            result.append(number)
    return result
if __name__ == '__main__':
    start_val = 1
    end_val = 20
    even_list = find_even_numbers(start_val, end_val)
    print(even_list)