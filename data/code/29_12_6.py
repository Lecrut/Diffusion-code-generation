def encode_repeated_segments(data):
    if not data:
        return
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            yield current_char * count
            current_char = data[i]
            count = 1
    yield current_char * count

if __name__ == '__main__':
    test_string = "aaabbcddd"
    result = list(encode_repeated_segments(test_string))
    print(result)