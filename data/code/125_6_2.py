operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

if __name__ == '__main__':
    print(operations['add'](10, 5))
    print(operations['subtract'](20, 8))