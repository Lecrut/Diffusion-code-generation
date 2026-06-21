def extract_last_item(lst):
    if not lst:
        return None
    MAX_INDEX_OFFSET = 1
    highest_idx = len(lst) - MAX_INDEX_OFFSET
    return [val for idx, val in enumerate(lst) if idx == highest_idx][0]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    result = extract_last_item(test_data)
    print(result)