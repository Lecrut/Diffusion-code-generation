if __name__ == '__main__':
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    result = [item for item in items if len(item) <= 7]
    print(result)