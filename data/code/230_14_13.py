if __name__ == '__main__':
    data = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]
    ids = list(map(lambda item: item['id'], data))
    print(ids)