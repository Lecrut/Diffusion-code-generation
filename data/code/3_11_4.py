VOWELS = set("aeiouAEIOU")

def strip_vowels(text):
    return "".join([char for char in text if char not in VOWELS])

if __name__ == "__main__":
    sample_text = "Hello World"
    result = strip_vowels(sample_text)
    print(result)