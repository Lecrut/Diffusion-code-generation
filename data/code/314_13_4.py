if __name__ == '__main__':
    input_string = "10,25,33,invalid,42"
    numbers = []
    is_numeric = True
    for item in input_string.split(','):
        try:
            numbers.append(int(item.strip()))
        except ValueError:
            is_numeric = False
            break
    total_sum = 0
    if is_numeric:
        total_sum = sum(numbers)
    print(f"The total sum is: {total_sum}")