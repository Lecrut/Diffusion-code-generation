import re
def tokenize_and_unique(text):
    words = re.findall(r'[a-zA-Z]+', text)
    unique_words = set()
    for word in words:
        unique_words.add(word.lower())
    return list(unique_words)
if __name__ == '__main__':
    sample_text1 = "Hello World! This is a test string, with numbers 123 and symbols @."
    sample_text2 = "Programming is fun; let's learn Python and data science."
    sample_text3 = "A B C a b c A b c"
    result1 = tokenize_and_unique(sample_text1)
    print(f"'{sample_text1}' -> {result1}")
    result2 = tokenize_and_unique(sample_text2)
    print(f"'{sample_text2}' -> {result2}")
    result3 = tokenize_and_unique(sample_text3)
    print(f"'{sample_text3}' -> {result3}")