def rle_stream_chunked(input_string, chunk_size=100):
    def get_rle_encoding(s):
        if not s:
            return []
        chunks = []
        count = 1
        prev_char = s[0]
        for char in s[1:]:
            if char == prev_char:
                count += 1
            else:
                chunks.append((prev_char, count))
                prev_char = char
                count = 1
        chunks.append((prev_char, count))
        return chunks

    current_buffer = []
    buffer_count = 0
    
    for char in input_string:
        current_buffer.append(char)
        buffer_count += 1
        if buffer_count >= chunk_size:
            yield get_rle_encoding(''.join(current_buffer))
            current_buffer = []
            buffer_count = 0
    
    if current_buffer:
        yield get_rle_encoding(''.join(current_buffer))

if __name__ == '__main__':
    sample_data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    generator = rle_stream_chunked(sample_data, chunk_size=25)
    for chunk in generator:
        print(chunk)