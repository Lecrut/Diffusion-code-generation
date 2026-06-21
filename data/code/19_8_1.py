def rle_chunk_generator(data, chunk_size):
    def get_rle(sequence):
        if not sequence:
            return sequence
        result = []
        current_char = sequence[0]
        count = 1
        for char in sequence[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{current_char}{count}")
                current_char = char
                count = 1
        result.append(f"{current_char}{count}")
        return "".join(result)

    i = 0
    n = len(data)
    while i < n:
        end = min(i + chunk_size, n)
        yield get_rle(data[i:end])
        i = end

if __name__ == "__main__":
    sample_input = "AAABBBCCCCDDDEEEFFFFFGGGGGHHHH"
    chunk_size = 5
    for chunk in rle_chunk_generator(sample_input, chunk_size):
        print(chunk)