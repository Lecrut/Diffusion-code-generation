def rle_chunks(stream, chunk_size=10):
    count = 0
    current_char = None
    buffer = []
    
    for char in stream:
        if char != current_char:
            if current_char is not None:
                buffer.append((current_char, count))
                count = 0
            current_char = char
        count += 1
        
        if count >= chunk_size:
            while buffer:
                yield buffer.pop(0)
            count = 0
            current_char = None
            
    if current_char is not None:
        buffer.append((current_char, count))
        
    while buffer:
        yield buffer.pop(0)

if __name__ == '__main__':
    sample_data = "AAABBBCCCCDDDDDDDDEEE"
    for encoded_chunk in rle_chunks(sample_data, 3):
        print(encoded_chunk)