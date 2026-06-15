if __name__ == '__main__':
    input_line = "10 20 30 40 50"
    numbers = input_line.split()
    total_sum = 0
    for num_str in numbers:
        number = int(num_str)
        total_sum += number
    print(total_sum)