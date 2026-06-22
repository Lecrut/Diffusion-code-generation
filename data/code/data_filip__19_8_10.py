def rle_encode_chunks(input_stream, chunk_size=1024):
    buffer = []
    current_char = None
    count = 0
    for char in input_stream:
        if current_char is None:
            current_char = char
            count = 1
        elif char == current_char:
            count += 1
        else:
            if buffer:
                yield ''.join(buffer)
                buffer = []
            if count == 1:
                buffer.append(current_char)
            else:
                buffer.append(str(count))
                buffer.append(current_char)
            current_char = char
            count = 1
        if len(buffer) > chunk_size:
            yield ''.join(buffer)
            buffer = []
    if current_char is not None:
        if buffer:
            yield ''.join(buffer)
            buffer = []
        if count == 1:
            buffer.append(current_char)
        else:
            buffer.append(str(count))
            buffer.append(current_char)
    if buffer:
        yield ''.join(buffer)
if __name__ == '__main__':
    sample_input = 'AAABBCDDDEEEEF'
    encoded_chunks = list(rle_encode_chunks(iter(sample_input), chunk_size=5))
    for chunk in encoded_chunks:
        print(chunk)