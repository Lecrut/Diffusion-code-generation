def count_vowels(word):
    """Count vowels in a single string (both lowercase 'aeiou' and uppercase)."""
    return sum(1 for char in word if char.lower() in "aeiou")

def vowel_counts_for_list(string_list):
    """Accepts a list of strings and returns a dictionary mapping each string to its vowel count."""
    result = {}
    for item in string_list:
        result[item] = count_vowels(item)
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements. No user input or external dependencies needed.
    test_input = ["hello", "world", "", "aeiou", "AEIOU"]

    output_dict = vowel_counts_for_list(test_input)

    print("Input:", test_input)
    print("Vowel counts:")
    for key, value in sorted(output_dict.items()):
        # Sorting keys ensures deterministic output format.
        if isinstance(key, str):
            display_key = key  # Strings are safe to display directly here as per task constraints (no formatting requests).
        else:
            try:
                display_key = f"'{key}'"
            except TypeError:
                display_key = str(key)

        print(f"{display_key}: {value}")