NUMBERS_TO_APPEND = list(range(1, 6))

def append_numbers(numbers_list):
    numbers_list.extend(NUMBERS_TO_APPEND)
    return numbers_list

if __name__ == '__main__':
    result = append_numbers([])
    print(result)