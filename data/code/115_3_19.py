if __name__ == '__main__':
    operations = {'divide': lambda x, y: x / y}
    result1 = operations['divide'](20, 5)
    result2 = operations['divide'](15.5, 3.0)
    print(f"Result of division: {result1}, {result2}")