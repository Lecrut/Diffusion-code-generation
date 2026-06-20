def compare_values(a, b):
    return a == b
if __name__ == '__main__':
    print(compare_values(5, 5))
    print(compare_values(5, 6))
    print(compare_values('hello', 'hello'))
    print(compare_values('hello', 'world'))