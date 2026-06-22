def get_middle(seq):
    try:
        seq = list(seq)
        length = len(seq)
        if length == 0:
            return None
        if length == 1:
            return seq[0]
        mid_index = length // 2
        if length % 2 == 1:
            return seq[mid_index]
        else:
            return [seq[mid_index - 1], seq[mid_index]]
    except Exception:
        return None

if __name__ == '__main__':
    print(get_middle([1, 2, 3, 4, 5]))
    print(get_middle([1, 2, 3, 4]))
    print(get_middle([1]))
    print(get_middle([]))
    print(get_middle([10, 20]))