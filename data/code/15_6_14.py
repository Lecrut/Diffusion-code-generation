def compress_sequence(input_string):
    if not input_string:
        return []
    
    compressed = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = char
            count = 1
    
    compressed.append((current_char, count))
    return compressed

def generate_compressed_strings(compressed_data):
    for char, count in compressed_data:
        yield char * count

def process_and_compress(input_string):
    compressed = compress_sequence(input_string)
    reconstructed = ''.join(generate_compressed_strings(compressed))
    return {
        'compressed': compressed,
        'reconstructed': reconstructed
    }

if __name__ == '__main__':
    input_seq = 'zzzzzxyyy'
    result = process_and_compress(input_seq)
    print(result['compressed'])
    print(result['reconstructed'])