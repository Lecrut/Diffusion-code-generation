def reverse_alphabet_triangle(start_char, end_char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if start_char in alphabet and end_char in alphabet:
        start_index = alphabet.index(start_char)
        end_index = alphabet.index(end_char)
        if start_index > end_index:
            reverse_alpha = alphabet[end_index : start_index + 1]
            sequence = reverse_alpha[::-1]
        else:
            sequence = alphabet[end_index : start_index - 1 if start_index else None : -1]
            if not sequence:
                sequence = [alphabet[end_index]]
        lines = []
        for i in range(len(sequence)):
            current_char = sequence[i]
            row = ""
            for j in range(i + 1):
                row += current_char
            lines.append(row)
        return "\n".join(lines)
    return ""

if __name__ == '__main__':
    result = reverse_alphabet_triangle('z', 'a')
    print(result)