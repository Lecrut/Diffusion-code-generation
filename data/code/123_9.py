if __name__ == '__main__':
    input_string = "10,25,3.5,40"
    numbers = input_string.split(',')
    total_sum = 0
    for item in numbers:
        try:
            total_sum += float(item.strip())
        except ValueError:
            pass
    print(total_sum)