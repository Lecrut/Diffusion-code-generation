def contains_in_stream(stream, element):
    return any(item == element for item in stream)

if __name__ == '__main__':
    sample_stream = (i for i in [1, 5, 2, 8, 3, 5])
    print(f"Checking for 2: {contains_in_stream(sample_stream, 2)}")
    print(f"Checking for 5: {contains_in_stream(sample_stream, 5)}")
    print(f"Checking for 9: {contains_in_stream(sample_stream, 9)}")