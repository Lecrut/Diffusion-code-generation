if __name__ == '__main__':
    result = (lambda x, y: f'Error: Division by zero' if y == 0 else f'{x / y:.2f}')(150.75, 3.0)
    print(result)