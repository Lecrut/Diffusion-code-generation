count_vowels = lambda text: sum(1 for char in text.lower() if char in "aeiou")
if __name__ == "__main__":
    sample_input = "The quick brown fox jumps over the lazy dog"
    result = count_vowels(sample_input)
    print(result)