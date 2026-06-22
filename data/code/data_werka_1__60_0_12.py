def fetch_last_item(sequence):
    if not sequence:
        return None
    return sequence[-1]

if __name__ == '__main__':
    TEST_LIST = [10, 20, 30, 40, 50]
    LAST_ITEM = fetch_last_item(TEST_LIST)
    print(LAST_ITEM)