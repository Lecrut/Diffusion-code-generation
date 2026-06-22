def append_numbers(start: int, end: int) -> list:
    numbers = []
    for i in range(start, end + 1):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    start_value = 1
    end_value = 5
    result = append_numbers(start_value, end_value)
    print(result)