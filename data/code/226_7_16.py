def duplicate_list():
    original = [True, False]
    result = []
    for _ in range(10):
        result += original[:]
    return result

if __name__ == '__main__':
    output = duplicate_list()
    print(output)