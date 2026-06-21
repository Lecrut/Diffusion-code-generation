def retrieve_last(seq):
    if not seq:
        raise IndexError("cannot get last element of empty sequence")
    return seq[-1]

if __name__ == '__main__':
    data = [100, 200, 300]
    print(retrieve_last(data))