def rle_chunk_generator(data):
    if not data:
        return
    iterator = iter(data)
    try:
        current_char = next(iterator)
    except StopIteration:
        return
    count = 1
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)

if __name__ == '__main__':
    sample_stream = "AAABBBCCCCDDDDEEEFFFF"
    encoded_chunks = list(rle_chunk_generator(sample_stream))
    print(encoded_chunks)