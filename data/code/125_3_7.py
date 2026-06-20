if __name__ == '__main__':
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y
    }
    result_add = operations['add'](20, 10)
    result_subtract = operations['subtract'](30, 5)
    print(f"Sum: {result_add}")
    print(f"Difference: {result_subtract}")