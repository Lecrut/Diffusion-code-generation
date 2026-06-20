def remove_vowels(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) == 0:
        return ""
    vowels = frozenset("aeiouAEIOU")
    return "".join(c for c in text if c not in vowels)

if __name__ == '__main__':
    input_string = "Algorithmic Complexity"
    output_string = remove_vowels(input_string)
    print(output_string)