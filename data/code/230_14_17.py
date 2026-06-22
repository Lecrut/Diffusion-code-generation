if __name__ == '__main__':
    data = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]
    
    try:
        ids = list(map(lambda x: x['id'], data))
        print(ids)
    except KeyError as e:
        print(f"Error: Dictionary missing 'id' key - {e}")