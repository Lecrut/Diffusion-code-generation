def duplicate_list():
    original = [True, False] * 5
    result = original[:]
    for _ in range(9):
        result += original
    return result

if __name__ == '__main__':
    print(duplicate_list())