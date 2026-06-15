if __name__ == '__main__':
    data = [3, 1, 8, 4, 5]
    if not data:
        max_element = None
    else:
        max_element = data[0]
        for i in range(1, len(data)):
            if data[i] > max_element:
                max_element = data[i]
    print(max_element)