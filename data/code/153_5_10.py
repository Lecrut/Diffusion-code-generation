def item_exists_in_stream(item, stream):
    return any(x == item for x in stream)

if __name__ == '__main__':
    sample_item = 5
    sample_stream = (x for x in range(10))
    print(item_exists_in_stream(sample_item, sample_stream))