if __name__ == '__main__':
    result = lambda x, y: x / y if y != 0 else 'Division by zero'
    print(result(150.75, 3.0))