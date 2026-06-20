def is_greater(x, y):
    return x > y
if __name__ == '__main__':
    try:
        result1 = is_greater(5, 3)
        print(f'Is 5 greater than 3? {result1}')
        result2 = is_greater(2, 4)
        print(f'Is 2 greater than 4? {result2}')
        result3 = is_greater('a', 3)
    except TypeError as e:
        print(f'Error: {e}')