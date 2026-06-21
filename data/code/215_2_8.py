if __name__ == '__main__':
    numbers = [100, 200, 50, 300, 75]
    max_value = None
    for number in numbers:
        if max_value is None or number > max_value:
            max_value = number
    print(max_value)