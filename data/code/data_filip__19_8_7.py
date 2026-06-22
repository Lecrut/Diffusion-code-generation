def rle_chunks(data_source, chunk_size=1024):
    yield from (
        (char, count)
        for chunk in data_source
        for count in (
            len(list(t))
            for _, t in __import__('itertools').groupby(chunk)
        )
        for char in (chunk[0] if chunk else None)
        if char is not None
    )

def process_large_stream(stream, chunk_size=1024):
    return rle_chunks(stream, chunk_size)

if __name__ == '__main__':
    sample_data = ["aabbbcc", "dddeefff", "ggggh"]
    result = list(process_large_stream(sample_data, chunk_size=1))
    print(result)