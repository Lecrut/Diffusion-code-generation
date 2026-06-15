if __name__ == '__main__':
    data = [3, 1, 8, 4, 5]
    if not data:
        max_value = None
    else:
        max_value = data[0]
        for i in range(1, len(data)):
            if data[i] > max_value:
                max_value = data[i]
    print(max_value)