def rle_encode_stream(text):
    if not text:
        return
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char and count < 255:
            count += 1
        else:
            yield current_char, count
            current_char = char
            count = 1
    yield current_char, count

def rle_decode_stream(encoded_chunks):
    for char, count in encoded_chunks:
        yield char * count

def chunked_rle_encoder(data_stream, chunk_size=1024):
    buffer = ""
    for char in data_stream:
        buffer += char
        if len(buffer) >= chunk_size:
            yield from rle_encode_stream(buffer)
            buffer = ""
    if buffer:
        yield from rle_encode_stream(buffer)

if __name__ == '__main__':
    sample_text = "AAAABBBCCDAA"
    encoded_chunks = list(rle_encode_stream(sample_text))
    print(encoded_chunks)
    decoded_text = "".join(rle_decode_stream(encoded_chunks))
    print(decoded_text)
    large_sample = "A" * 10000 + "B" * 5000 + "C" * 3000
    lazy_encoded = list(chunked_rle_encoder(iter(large_sample), chunk_size=100))
    print(lazy_encoded[:5])
    lazy_decoded = "".join(rle_decode_stream(iter(lazy_encoded)))
    print(lazy_decoded == large_sample)