def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    result = check_match(42, 42)
    print(result)
    result = check_match('hello', 'world')
    print(result)
    result = check_match([1, 2, 3], [1, 2, 3])
    print(result)
    result = check_match({'key': 'value'}, {'key': 'value'})
    print(result)