def bidirectional_rle(input_string: str) -> dict:
    if not input_string:
        compressed = ''
    else:
        compressed_chars = []
        current_char = input_string[0]
        count = 1
        for char in input_string[1:]:
            if char == current_char:
                count += 1
            else:
                compressed_chars.append(str(count) + current_char)
                current_char = char
                count = 1
        compressed_chars.append(str(count) + current_char)
        compressed = ''.join(compressed_chars)
    if not compressed:
        decompressed = ''
    else:
        decompressed_chars = []
        i = 0
        while i < len(compressed):
            count_str = ''
            while i < len(compressed) and compressed[i].isdigit():
                count_str += compressed[i]
                i += 1
            if i < len(compressed):
                char = compressed[i]
                i += 1
                if count_str:
                    decompressed_chars.append(char * int(count_str))
                else:
                    decompressed_chars.append(char)
        decompressed = ''.join(decompressed_chars)
    is_integrity_ok = decompressed == input_string
    return {'original': input_string, 'compressed': compressed, 'decompressed': decompressed, 'integrity_ok': is_integrity_ok}
if __name__ == '__main__':
    test_strings = ['AABCCCCDEEEE', '', 'XYZXYZXYZ', 'AAAAABBBBCCCCCCCCCC', 'SingleChar']
    results = []
    for s in test_strings:
        result = bidirectional_rle(s)
        results.append(result)
        print(result['original'], result['compressed'], result['decompressed'], result['integrity_ok'])
    final_output = {'test_passed': all((r['integrity_ok'] for r in results)), 'total_tests': len(results), 'results': results}
    print(final_output)