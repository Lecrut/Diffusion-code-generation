def find_first_element(items):
    for item in items:
        return item
if __name__ == '__main__':
    data = [10, 20, 30]
    result = find_first_element(data)
    print(result)