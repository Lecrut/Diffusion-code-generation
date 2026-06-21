def numeric_to_text(key):
    mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    return mapping.get(key, None)
if __name__ == '__main__':
    print(numeric_to_text(3))
    print(numeric_to_text(6))