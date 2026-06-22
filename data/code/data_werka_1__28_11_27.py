def determine_larger(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2

if __name__ == '__main__':
    result = determine_larger(10.5, 20)
    print(result)