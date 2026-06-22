def find_minimum(data):
    if not data:
        raise ValueError('Input list cannot be empty')
    minimum = data[0]
    for string in data[1:]:
        if string < minimum:
            minimum = string
    return minimum
if __name__ == '__main__':
    input_data = ['apple', 'banana', 'cherry']
    try:
        result = find_minimum(input_data)
        print(result)
    except ValueError as e:
        print(e)