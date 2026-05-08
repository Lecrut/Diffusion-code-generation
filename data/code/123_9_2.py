if __name__ == '__main__':
    input_string = "10,5,22,8"
    numbers = input_string.split(',')
    total_sum = 0
    for num_str in numbers:
        try:
            total_sum += int(num_str.strip())
        except ValueError:
            pass
    print(total_sum)