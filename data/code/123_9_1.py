if __name__ == '__main__':
    input_string = "10,25,5,15.5"
    numbers = input_string.split(',')
    total_sum = 0
    for num_str in numbers:
        try:
            total_sum += float(num_str.strip())
        except ValueError:
            pass
    print(total_sum)