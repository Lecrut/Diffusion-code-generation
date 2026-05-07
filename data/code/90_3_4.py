def check_or_condition(a, b):
    try:
        result = a or b
        return result
    except TypeError:
        return False
if __name__ == '__main__':
    value1 = 10
    value2 = 0
    result = check_or_condition(value1, value2)
    print(result)