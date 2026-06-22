def generate_number_list(start: int, end: int) -> list:
    numbers = []
    for i in range(start, end + 1):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    start_value = 1
    end_value = 5
    number_list = generate_number_list(start_value, end_value)
    print(number_list)