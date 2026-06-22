def check_first_and_last(data):
    if not data:
        raise ValueError("Input sequence must not be empty")
    lookup = {"start": 0, "end": -1}
    indices = (lookup["start"], lookup["end"])
    return data[indices[0]], data[indices[1]]

if __name__ == '__main__':
    values = [7, 8, 9, 10]
    result = check_first_and_last(values)
    print(result)