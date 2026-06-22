def compress_sequence(seq: str) -> str:
    if not seq:
        return ''
    result = []
    current_char = seq[0]
    count = 1
    for char in seq[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f'{count}{current_char}')
            current_char = char
            count = 1
    result.append(f'{count}{current_char}')
    return ''.join(result)

def run_compression_demo() -> None:
    sequence = 'zzzzzxyyy'
    compressed = compress_sequence(sequence)
    print(f'Original: {sequence}')
    print(f'Compressed: {compressed}')
if __name__ == '__main__':
    run_compression_demo()