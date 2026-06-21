def retrieve_penultimate(sequence):
    if len(sequence) < 2:
        return None
    return sequence[-2]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    value = retrieve_penultimate(test_data)
    print(value)