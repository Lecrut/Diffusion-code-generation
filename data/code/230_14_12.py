if __name__ == '__main__':
    data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    
    ids = list(map(lambda item: item['id'], data))
    print(ids)