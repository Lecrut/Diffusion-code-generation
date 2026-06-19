def swap_adjacent_characters(s):
    chars = list(s)
    swapped_chars = [chars[i + 1] + chars[i] if i % 2 == 0 else chars[i] for i in range(len(chars) - 1)]
    if len(s) % 2 != 0:
        swapped_chars.append(chars[-1])
    return ''.join(swapped_chars)
if __name__ == '__main__':
    sample_string = 'abcdefg'
    result = swap_adjacent_characters(sample_string)
    print(result)