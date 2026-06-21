def item_exists_in_stream(item, stream):
    return any(x == item for x in stream)

if __name__ == '__main__':
    sample_item = 'apple'
    sample_stream = iter(['banana', 'apple', 'cherry'])
    print(item_exists_in_stream(sample_item, sample_stream))