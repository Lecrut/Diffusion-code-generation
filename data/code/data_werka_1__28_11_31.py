def determine_larger(value1, value2):
    return value1 if value1 > value2 else value2

if __name__ == '__main__':
    result = determine_larger(42, 3.14)
    print(result)