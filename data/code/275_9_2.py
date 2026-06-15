if __name__ == '__main__':
    data = [3.14, 1.618, 2.718, 0.577, 4.0]
    if not data:
        max_value = None
    else:
        max_value = data[0]
        for i in range(1, len(data)):
            if data[i] > max_value:
                max_value = data[i]
    print(max_value)