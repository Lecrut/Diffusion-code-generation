if __name__ == '__main__':
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y
    }
    
    result_add = operations['add'](15, 7)
    result_subtract = operations['subtract'](15, 7)
    
    print(f"Sum: {result_add}")
    print(f"Difference: {result_subtract}")