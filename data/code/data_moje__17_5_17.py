def retrieve_last(seq):
    if not seq:
        raise IndexError("Sequence empty")
    return seq[-1]

if __name__ == '__main__':
    data = [5, 15, 25, 35]
    print(retrieve_last(data))