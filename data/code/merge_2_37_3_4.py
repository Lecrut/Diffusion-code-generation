def consolidate_items(*args):
    result = {}
    for item in args:
        if isinstance(item, tuple) and len(item) == 2:
            key, count = item[0], int(item[1])
            result[key] = result.get(key, 0) + count
        else:
            raise ValueError(f"Invalid input format. Expected (item, count), got {type(item)}")
    return result
if __name__ == '__main__':
    data = ('apple', 3), ('banana', 5), ('apple', 2), ('cherry', 10)
    totals = consolidate_items(*data)
    print(totals)