def rle_chunks(input_stream, chunk_size=1024):
    current_char = None
    count = 0
    buffer = []
    
    for char in input_stream:
        buffer.append(char)
        if len(buffer) > chunk_size:
            yield ''.join(buffer)
            buffer = []
            current_char = None
            count = 0
            continue
        
        if current_char is None:
            current_char = char
            count = 1
        elif char == current_char:
            count += 1
            if count > 255:
                buffer = buffer[:-count]
                buffer.append(f"{current_char}{count}")
                current_char = char
                count = 0
        else:
            if count > 0:
                if count > 1:
                    buffer.append(f"{current_char}{count}")
                else:
                    buffer.append(current_char)
            current_char = char
            count = 1
    
    if count > 0:
        if count > 1:
            buffer.append(f"{current_char}{count}")
        else:
            buffer.append(current_char)
    
    if buffer:
        yield ''.join(buffer)

def generate_large_stream():
    for i in range(1000000):
        if i % 3 == 0:
            yield 'A'
        elif i % 3 == 1:
            yield 'B'
        else:
            yield 'C'

if __name__ == '__main__':
    stream = generate_large_stream()
    chunks = rle_chunks(stream, chunk_size=50)
    for i, chunk in enumerate(chunks):
        if i < 5:
            print(chunk)
        else:
            break