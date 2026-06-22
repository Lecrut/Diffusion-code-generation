def rle_stream_chunks(input_string, chunk_size=1024):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")
    if not input_string:
        return iter([])
    
    iterator = iter(input_string)
    current_char = next(iterator, None)
    
    def count_char(char):
        count = 1
        next_char = next(iterator, None)
        while next_char == char:
            count += 1
            next_char = next(iterator, None)
        return count, next_char

    remaining_buffer = ""
    
    for char in input_string:
        remaining_buffer += char
        while len(remaining_buffer) >= chunk_size:
            chunk = remaining_buffer[:chunk_size]
            remaining_buffer = remaining_buffer[chunk_size:]
            
            current_index = 0
            while current_index < len(chunk):
                c = chunk[current_index]
                count = 1
                while current_index + count < len(chunk) and chunk[current_index + count] == c:
                    count += 1
                yield (c, count)
                current_index += count

if __name__ == '__main__':
    test_string = "AAABBBCCCDDEEEF"
    chunks = list(rle_stream_chunks(test_string, chunk_size=5))
    print(chunks)