def rle_encode(data):
    if not data:
        return
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            yield current_char, count
            current_char = char
            count = 1
    yield current_char, count

def rle_decode(encoded_data):
    for char, count in encoded_data:
        for _ in range(count):
            yield char

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    print(list(rle_encode(sample_string)))
    encoded = list(rle_encode(sample_string))
    print("".join(rle_decode(encoded)))