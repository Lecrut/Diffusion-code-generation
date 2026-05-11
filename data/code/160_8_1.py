if __name__ == '__main__':
    items = ["apple", "banana", "kiwi", "orange"]
    result = {item: len(item) for item in items}
    print(result)