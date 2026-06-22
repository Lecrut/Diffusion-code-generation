def duplicate_boolean_list():
    original_list = [True, False]
    result = []
    for _ in range(10):
        result += original_list
    return result

if __name__ == '__main__':
    output = duplicate_boolean_list()
    print(output)