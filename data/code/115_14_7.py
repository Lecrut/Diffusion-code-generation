if __name__ == '__main__':
    DIVISOR = 3.0
    
    result = (lambda x, y: x / y if y != 0 else 'Division by zero')(150.75, DIVISOR)
    print(result)