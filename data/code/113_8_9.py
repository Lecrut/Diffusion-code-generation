def subtract(a, b):
    return a - b

if __name__ == '__main__':
    operations = {
        '10-5': (10, 5),
        '5-10': (5, 10),
        '10-10': (10, 10),
        '-10-5': (-10, 5),
        '5--10': (5, -10),
        '-10--5': (-10, -5),
        '-10--10': (-10, -10)
    }
    
    for operation, (a, b) in operations.items():
        result = subtract(a, b)
        print(f"{operation} = {result}")