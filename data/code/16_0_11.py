def fetch_head_item(sequence):
    return sequence[0]

if __name__ == '__main__':
    VALUES = [7, 14, 21, 28]
    head = fetch_head_item(VALUES)
    print(head)