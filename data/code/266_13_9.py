def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    sample_text1 = "This is a sample sentence."
    sample_text2 = "  Multiple   spaces here."
    sample_text3 = ""
    sample_text4 = "SingleWord"
    
    print(f"'{sample_text1}': {count_words(sample_text1)}")
    print(f"'{sample_text2}': {count_words(sample_text2)}")
    print(f"'{sample_text3}': {count_words(sample_text3)}")
    print(f"'{sample_text4}': {count_words(sample_text4)}")