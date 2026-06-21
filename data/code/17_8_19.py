def retrieve_final_item(collection):
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Argument must be a sequence")
    if len(collection) == 0:
        raise ValueError("Sequence cannot be empty")
    return collection[-1]

if __name__ == '__main__':
    items = [100, 200, 300, 400, 500]
    final_val = retrieve_final_item(items)
    print(final_val)