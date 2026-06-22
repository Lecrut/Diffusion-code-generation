def extract_pair(list_a, list_b, idx):
    try:
        val_a = list_a[idx]
    except IndexError:
        raise ValueError("Index out of range for list_a")
    try:
        val_b = list_b[idx]
    except IndexError:
        raise ValueError("Index out of range for list_b")
    return [(val_a, val_b)]

if __name__ == '__main__':
    source_1 = [100, 200, 300]
    source_2 = [400, 500, 600]
    position = 2
    data = extract_pair(source_1, source_2, position)
    print(data)