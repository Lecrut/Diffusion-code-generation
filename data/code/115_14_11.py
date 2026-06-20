if __name__ == '__main__':
    try:
        result = (lambda x, y: x / y)(150.75, 3.0)
        print(result)
    except ZeroDivisionError:
        print('Division by zero')