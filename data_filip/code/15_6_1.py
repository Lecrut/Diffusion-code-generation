import zlib

def process_and_compress_sequence(sequence):
    run_length_encoded = run_length_encode(sequence)
    compressed = zlib.compress(sequence.encode('utf-8'))
    return (list(run_length_encoded), compressed)

def run_length_encode(sequence):
    if not sequence:
        return
    current_char = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current_char:
            count += 1
        else:
            yield (current_char, count)
            current_char = char
            count = 1
    yield (current_char, count)
if __name__ == '__main__':
    sample_sequence = 'zzzzzxyyy'
    rle_result, compressed_result = process_and_compress_sequence(sample_sequence)
    print(rle_result)
    print(compressed_result)