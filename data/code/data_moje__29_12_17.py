def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    sample_text = "Hello World! This is a sample string with vowels."
    print(count_vowels(sample_text))