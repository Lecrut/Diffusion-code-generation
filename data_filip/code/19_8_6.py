def rle_chunked_generator(data, chunk_size):
    def process_chunk(chunk):
        if not chunk:
            return
        count = 1
        length = len(chunk)
        for i in range(1, length):
            if chunk[i] == chunk[i - 1]:
                count += 1
            else:
                yield chunk[i - 1], count
                count = 1
        yield chunk[-1], count

    start = 0
    length = len(data)
    while start < length:
        end = min(start + chunk_size, length)
        current_chunk = data[start:end]
        for char, count in process_chunk(current_chunk):
            yield char, count
        start = end

def main():
    sample_data = "AAABBBCCCCDDDDEEEEE" * 100
    chunk_size = 50
    result = []
    for char, count in rle_chunked_generator(sample_data, chunk_size):
        result.append(f"{char}{count}")
    print("".join(result))

if __name__ == '__main__':
    main()