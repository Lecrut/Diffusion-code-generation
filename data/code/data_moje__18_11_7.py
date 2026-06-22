def extract_middle(data):
    indices = {"odd": "len(data) // 2", "even": "len(data) // 2"}
    count = len(data)
    lookup_key = "odd" if count % 2 != 0 else "even"
    index_expr = indices[lookup_key]
    offset = eval(index_expr)
    return data[offset]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    print(extract_middle(test_data))