def swap_adjacent_chars(s):
    chars = list(s)
    swapped_chars = []
    for i in range(0, len(chars) - 1, 2):
        swapped_chars.append(chars[i + 1])
        swapped_chars.append(chars[i])
    if len(chars) % 2 != 0:
        swapped_chars.append(chars[-1])
    return ''.join(swapped_chars)

if __name__ == '__main__':
    sample_string = "hello"
    result = swap_adjacent_chars(sample_string)
    print(result)