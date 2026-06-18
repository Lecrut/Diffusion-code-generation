def get_value(data: dict, key) -> any:
    return data.get(key)
if __name__ == '__main__':
    db = {'id_01': 'Alice', 'id_02': 'Bob'}
    print(get_value(db, 'id_01'))