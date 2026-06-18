def find_initial_item(items):
    for item in items:
        if item is not None and str(item).strip():
            return item
    return None
if __name__ == '__main__':
    sample_list = [None, "", "  ", [], {}, (), 0, False, True]
    result = find_initial_item(sample_list)
    print(result if result is not None else "No valid initial item found")