if __name__ == '__main__':
    operations = {
        'divide': lambda x, y: x / y if y != 0 else 'Division by zero'
    }
    result = operations['divide'](150.75, 3.0)
    print(result)