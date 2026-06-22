def build_number_list(start: int, end: int) -> list:
    number_list = []
    for num in range(start, end + 1):
        number_list.append(num)
    return number_list

if __name__ == '__main__':
    start_value = 1
    end_value = 5
    result_list = build_number_list(start_value, end_value)
    print(result_list)