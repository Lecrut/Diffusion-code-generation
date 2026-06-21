def rle_chunks(text, chunk_size=1000):
    if not text:
        return
    
    iterator = iter(text)
    try:
        current_char = next(iterator)
    except StopIteration:
        return
        
    count = 1
    buffer = []
    
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            buffer.append(f"{count}{current_char}")
            if len(buffer) >= chunk_size:
                yield "".join(buffer)
                buffer = []
            current_char = char
            count = 1
            
    buffer.append(f"{count}{current_char}")
    if buffer:
        yield "".join(buffer)

if __name__ == '__main__':
    sample_text = "AAABBBCCCD"
    result = list(rle_chunks(sample_text))
    print(result)