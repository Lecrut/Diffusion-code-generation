def item_exists_in_stream(stream, item):
    return any(x == item for x in stream)

if __name__ == '__main__':
    sample_stream = (x for x in [1, 5, 2, 8, 3, 5])
    print(f"Checking for 2: {item_exists_in_stream(sample_stream, 2)}")
    print(f"Checking for 5: {item_exists_in_stream(sample_stream, 5)}")
    print(f"Checking for 9: {item_exists_in_stream(sample_stream, 9)}")