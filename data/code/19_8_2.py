def rle_chunks(data, chunk_size=100):
    i = 0
    n = len(data)
    while i < n:
        current_char = data[i]
        count = 0
        while i < n and data[i] == current_char:
            count += 1
            i += 1
        yield (current_char, count)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDEEE"
    for char, count in rle_chunks(sample_string):
        print(f"{char}{count}", end="")
    print()