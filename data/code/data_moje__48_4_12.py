def generate_max(data):
    if not data:
        return
    current_max = data[0]
    for value in data:
        if value > current_max:
            current_max = value
        yield current_max

if __name__ == '__main__':
    inputs = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = max(generate_max(inputs))
    print(result)