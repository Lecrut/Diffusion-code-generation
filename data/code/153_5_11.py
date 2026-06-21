def item_exists_in_stream(stream, target):
    return any(item == target for item in stream)

if __name__ == '__main__':
    sample_stream = iter([1, 5, 2, 8, 3, 5])
    print(f"Checking for 2: {item_exists_in_stream(sample_stream, 2)}")
    print(f"Checking for 5: {item_exists_in_stream(sample_stream, 5)}")
    print(f"Checking for 9: {item_exists_in_stream(sample_stream, 9)}")
    print(f"Checking for 1: {item_exists_in_stream(sample_stream, 1)}")
    print(f"Checking for 8: {item_exists_in_stream(sample_stream, 8)}")