def rle_lazy_chunks(data, chunk_size=100):
    def encode_segment(segment):
        if not segment:
            return
        current_char = segment[0]
        count = 1
        for char in segment[1:]:
            if char == current_char:
                count += 1
            else:
                yield str(count) + current_char
                current_char = char
                count = 1
        yield str(count) + current_char

    length = len(data)
    i = 0
    while i < length:
        end = min(i + chunk_size, length)
        chunk = data[i:end]
        encoded_parts = list(encode_segment(chunk))
        if encoded_parts:
            yield "".join(encoded_parts)
        i = end

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDDDDEEEE"
    result = list(rle_lazy_chunks(sample_input, 5))
    print(result)