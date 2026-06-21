def rle_encode_chunked(data_stream, chunk_size=1024):
    def _rle_encode_segment(segment):
        if not segment:
            return []
        encoded = []
        current_char = segment[0]
        count = 1
        for char in segment[1:]:
            if char == current_char and count < 255:
                count += 1
            else:
                encoded.append((current_char, count))
                current_char = char
                count = 1
        encoded.append((current_char, count))
        return encoded

    def _stream_chunks(stream):
        while True:
            chunk = next(stream, None)
            if chunk is None:
                break
            yield chunk

    def _process_chunks():
        buffer = ""
        for chunk in _stream_chunks(data_stream):
            buffer += chunk
            if len(buffer) >= chunk_size:
                process_len = (len(buffer) // chunk_size) * chunk_size
                if process_len > 0:
                    segment = buffer[:process_len]
                    buffer = buffer[process_len:]
                    for char, count in _rle_encode_segment(segment):
                        yield f"{count}{char}"
        if buffer:
            for char, count in _rle_encode_segment(buffer):
                yield f"{count}{char}"

    return _process_chunks()

def string_to_iterator(s):
    chunk_size = 100
    for i in range(0, len(s), chunk_size):
        yield s[i:i + chunk_size]

if __name__ == "__main__":
    sample_string = "AAAABBBCCDAA" * 1000
    iterator = string_to_iterator(sample_string)
    encoder = rle_encode_chunked(iterator, chunk_size=200)
    encoded_chunks = list(encoder)
    print(encoded_chunks[:10])
    print(len(encoded_chunks))