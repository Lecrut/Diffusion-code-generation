if __name__ == '__main__':
    data = [3.14, 1.618, 2.718, 0.577, 4.0]
    if not data:
        max_value = None
    else:
        max_value = data[0]
        for number in data[1:]:
            if number > max_value:
                max_value = number
    print(max_value)