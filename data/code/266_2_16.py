from collections import defaultdict

WORD_DELIMITERS = " \n\t.,;:!?"

def count_word_frequency(text):
    if not text:
        return {}
    
    word_count = defaultdict(int)
    words = text.split()
    for word in words:
        clean_word = ''.join(char.lower() for char in word if char.isalnum())
        if clean_word:
            word_count[clean_word] += 1
    
    return dict(word_count)

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence, for testing."
    sample_text2 = "Another test case; with multiple words! Leading and trailing spaces are handled correctly.   "
    sample_text3 = ""
    
    freq1 = count_word_frequency(sample_text1)
    print(f"Text 1: '{sample_text1}'")
    print(f"Word Frequency: {freq1}\n")
    
    freq2 = count_word_frequency(sample_text2)
    print(f"Text 2: '{sample_text2}'")
    print(f"Word Frequency: {freq2}\n")
    
    freq3 = count_word_frequency(sample_text3)
    print(f"Text 3: '{sample_text3}'")
    print(f"Word Frequency: {freq3}\n")