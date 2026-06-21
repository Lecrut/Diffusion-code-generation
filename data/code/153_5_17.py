def stream_contains(stream, element):
    return any(item == element for item in stream)

if __name__ == '__main__':
    sample_stream = (1, 5, 2, 8, 3, 5)
    print(f"Checking for 2: {stream_contains(sample_stream, 2)}")
    print(f"Checking for 5: {stream_contains(sample_stream, 5)}")
    print(f"Checking for 9: {stream_contains(sample_stream, 9)}")
    print(f"Checking for 1: {stream_contains(sample_stream, 1)}")
    print(f"Checking for 8: {stream_contains(sample_stream, 8)}")