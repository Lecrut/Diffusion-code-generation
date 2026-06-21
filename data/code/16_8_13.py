def get_first_value():
    vector = [10, 20, 30, 40, 50]
    if not vector:
        raise ValueError("Vector is empty")
    return vector[0]

if __name__ == '__main__':
    result = get_first_value()
    print(result)