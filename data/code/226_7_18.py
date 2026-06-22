def duplicate_boolean_list():
    original_list = [True, False]
    result = original_list * 10
    return result

if __name__ == '__main__':
    output = duplicate_boolean_list()
    print(output)