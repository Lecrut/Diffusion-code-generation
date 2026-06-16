def remove_duplicates(items: list) -> set:
    return {item for item in items}
if __name__ == '__main__':
    data = [1, 2, 'a', 3, 'b', 4]
    result = remove_duplicates(data)
    print(result)