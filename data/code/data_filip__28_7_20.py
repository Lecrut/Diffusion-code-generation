def rle_generator(data):
    if not data:
        return
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            yield current_char, count
            current_char = data[i]
            count = 1
    yield current_char, count

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAA"
    result = list(rle_generator(sample_string))
    print(result)