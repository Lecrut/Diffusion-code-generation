operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

if __name__ == '__main__':
    result_add = operations['add'](5, 3)
    result_subtract = operations['subtract'](10, 4)
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_subtract}")