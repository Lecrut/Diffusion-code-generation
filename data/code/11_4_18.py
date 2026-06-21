def fetch_last_element(sequence):
    if type(sequence) is not list:
        raise TypeError("Input must be a list")
    if len(sequence) == 0:
        raise IndexError("Cannot access last item of an empty list")
    index = len(sequence) - 1
    return sequence[index]

if __name__ == '__main__':
    data = [100, 200, 300, 400, 500]
    result = fetch_last_element(data)
    print(result)