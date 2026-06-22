def rle_encode_stream(data_iterable, chunk_size=1024):
    current_char = None
    count = 0
    buffer = []
    
    def flush_buffer():
        nonlocal current_char, count, buffer
        if current_char is not None:
            buffer.append((current_char, count))
            current_char = None
            count = 0
        yield buffer
        buffer = []

    for char in data_iterable:
        if current_char is None:
            current_char = char
            count = 1
        elif char == current_char:
            count += 1
        else:
            buffer.append((current_char, count))
            current_char = char
            count = 1
        
        if len(buffer) >= chunk_size:
            yield from flush_buffer()
    
    if current_char is not None:
        buffer.append((current_char, count))
    
    if buffer:
        yield buffer

def rle_decode_chunks(chunks):
    for chunk in chunks:
        for char, count in chunk:
            yield from (char for _ in range(count))

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDEEEEEEFFFFGGGHH"
    
    encoded_chunks = list(rle_encode_stream(sample_string, chunk_size=3))
    print(encoded_chunks)
    
    decoded_string = "".join(rle_decode_chunks(encoded_chunks))
    print(decoded_string)