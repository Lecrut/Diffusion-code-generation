def rle_encode_stream(data_stream, chunk_size=1024):
    def rle_chunk_generator():
        buffer = ""
        for chunk in data_stream:
            buffer += chunk
            while len(buffer) >= chunk_size:
                processable = buffer[:chunk_size]
                buffer = buffer[chunk_size:]
                yield _rle_encode(processable)
        if buffer:
            yield _rle_encode(buffer)
    return rle_chunk_generator()

def _rle_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char and count < 99:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

def simulate_large_stream(data, chunk_size=100):
    start = 0
    while start < len(data):
        yield data[start:start + chunk_size]
        start += chunk_size

if __name__ == '__main__':
    sample_data = "AAABBBCCCCDDDDDDDEEEEEF"
    stream_generator = simulate_large_stream(sample_data, chunk_size=5)
    rle_chunks = rle_encode_stream(stream_generator, chunk_size=5)
    encoded_parts = list(rle_chunks)
    print("".join(encoded_parts))