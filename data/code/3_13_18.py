def _create_vowel_set():
    return frozenset('aeiouAEIOU')

VOWELS = _create_vowel_set()

def remove_vowels_from_text(text: str) -> str:
    target_chars = VOWELS
    filtered_chars = (
        char
        for char in text
        if char not in target_chars
    )
    return ''.join(filtered_chars)

if __name__ == '__main__':
    sample_input = "The quick brown fox jumps over the lazy dog"
    output_result = remove_vowels_from_text(sample_input)
    print(output_result)