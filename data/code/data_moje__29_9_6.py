def count_vowels_optimized(text: str) -> int:
    translation_map = str.maketrans("", "", "".join([c for c in "aeiouAEIOU"]))
    cleaned_text = text.translate(translation_map)
    return len(text) - len(cleaned_text)

if __name__ == "__main__":
    sample_string = "The quick brown fox jumps over the lazy dog. AaEeIiOoUu"
    result = count_vowels_optimized(sample_string)
    print(result)