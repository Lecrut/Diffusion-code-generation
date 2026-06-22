def get_last_item(seq):
    if len(seq) == 0:
        return None
    rev = reversed(seq)
    val = next(rev)
    return val

if __name__ == '__main__':
    items = [7, 8, 9, 10]
    print(get_last_item(items))