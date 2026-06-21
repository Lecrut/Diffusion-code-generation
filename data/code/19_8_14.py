def rle_chunks(data, chunk_size=4):
    if not data:
        return
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            if i % chunk_size == 0 or count >= 100:
                yield f"{data[i - 1]}{count}"
                count = 1
            else:
                yield f"{data[i - 1]}{count}"
                count = 1
    yield f"{data[-1]}{count}"

def rle_lazily_stream(data_stream, chunk_size=4):
    buffer = ""
    for char in data_stream:
        buffer += char
        if len(buffer) >= chunk_size:
            yield from rle_chunks(buffer[:chunk_size])
            buffer = buffer[chunk_size:]
    if buffer:
        yield from rle_chunks(buffer)

if __name__ == "__main__":
    sample_stream = "AAAABBBCCDAA"
    result_chunks = list(rle_lazily_stream(sample_stream))
    print(result_chunks)