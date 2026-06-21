def solve_unique_characters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    for char in text:
        if counts[char] == 1:
            return char
    return None

if __name__ == '__main__':
    sample_text = 'abacabad'
    unique_char = solve_unique_characters(sample_text)
    print(unique_char)