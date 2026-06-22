def append_numbers_to_list():
    numbers = []
    for i in range(1, 6):
        numbers.append(i)
    return numbers

if __name__ == '__main__':
    result = append_numbers_to_list()
    print(result)