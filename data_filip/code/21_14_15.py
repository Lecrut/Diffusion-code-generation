def run_length_encode(sequence):
    if not sequence:
        return []
    encoded = []
    current_char = sequence[0]
    count = 1
    for item in sequence[1:]:
        if item == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = item
            count = 1
    encoded.append((current_char, count))
    return encoded

if __name__ == '__main__':
    print(run_length_encode("AAABBBCCDAA"))
    print(run_length_encode("ABC"))
    print(run_length_encode("AAAAA"))
    print(run_length_encode("ABABAB"))
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("112233344444"))
    print(run_length_encode([1, 1, 1, 2, 2, 3]))