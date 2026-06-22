def get_last_element(sequence):
    try:
        return sequence[-1]
    except IndexError:
        raise ValueError("Sequence is empty")

if __name__ == '__main__':
    data = [5, 10, 15, 20]
    output = get_last_element(data)
    print(output)