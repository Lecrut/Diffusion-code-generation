def sum_three(a, b, c):
    return a + b + c
if __name__ == '__main__':
    try:
        result = sum_three(10, 20, 30)
        print(result)
    except TypeError as e:
        print(f'Error: {e}')