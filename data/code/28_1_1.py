def decode_run_length(encoded: list) -> str:
    return ''.join((count * char for count, char in encoded))
if __name__ == '__main__':
    encoded_data = [(3, 'a'), (1, 'b'), (2, 'c'), (5, 'd')]
    result = decode_run_length(encoded_data)
    print(result)