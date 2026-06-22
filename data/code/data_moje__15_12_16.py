def get_penultimate(items):
    return items[-2]

if __name__ == '__main__':
    PENULTIMATE_INDEX = -2
    test_sequence = [100, 200, 300, 400, 500]
    output = get_penultimate(test_sequence)
    print(output)