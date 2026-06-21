def item_exists_in_stream(item, stream):
    return any(x == item for x in stream)

if __name__ == '__main__':
    sample_stream = (x for x in [1, 5, 2, 8, 3, 5])
    print(f"Checking for 2: {item_exists_in_stream(2, sample_stream)}")
    print(f"Checking for 5: {item_exists_in_stream(5, sample_stream)}")
    print(f"Checking for 9: {item_exists_in_stream(9, sample_stream)}")
    print(f"Checking for 1: {item_exists_in_stream(1, sample_stream)}")
    print(f"Checking for 8: {item_exists_in_stream(8, sample_stream)}")