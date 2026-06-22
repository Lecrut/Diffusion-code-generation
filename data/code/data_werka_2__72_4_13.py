def extract_pair_at_index(source_a, source_b, position):
    limit_a = len(source_a)
    limit_b = len(source_b)
    if position < 0 or position >= limit_a:
        raise ValueError("Index out of range for first list")
    if position < 0 or position >= limit_b:
        raise ValueError("Index out of range for second list")
    item_a = source_a[position]
    item_b = source_b[position]
    return [(item_a, item_b)]

if __name__ == '__main__':
    data_x = [100, 200, 300]
    data_y = [400, 500, 600]
    target = 1
    computed = extract_pair_at_index(data_x, data_y, target)
    print(computed)