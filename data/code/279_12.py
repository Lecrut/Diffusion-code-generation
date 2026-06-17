def find_even_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            result.append(num)
    return result
if __name__ == '__main__':
    start_value = 1
    end_value = 20
    even_list = find_even_numbers(start_value, end_value)
    print(even_list)