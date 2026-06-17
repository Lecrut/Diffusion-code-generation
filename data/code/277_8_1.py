if __name__ == '__main__':
    input_line = "10 20 30 40 50"
    numbers_as_strings = input_line.split()
    numbers = []
    for item in numbers_as_strings:
        numbers.append(int(item))
    total_sum = 0
    for number in numbers:
        total_sum += number
    print(total_sum)