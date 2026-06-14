if __name__ == '__main__':
    data = [3.14, 1.618, 2.718, 0.577, 4.0]
    if not data:
        maximum = None
    else:
        maximum = data[0]
        for number in data[1:]:
            if number > maximum:
                maximum = number
    print(f"The list is: {data}")
    print(f"The maximum element is: {maximum}")