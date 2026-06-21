def check_match(value1, value2):
    if value1 is value2:
        return True
    if type(value1) != type(value2):
        return False
    return value1 == value2

if __name__ == '__main__':
    sample_value1 = (1, 2, 3)
    sample_value2 = (1, 2, 3)
    result = check_match(sample_value1, sample_value2)
    print(result)