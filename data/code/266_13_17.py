def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    paragraph1 = "This is a sample sentence."
    paragraph2 = "  Multiple   spaces here."
    paragraph3 = ""
    paragraph4 = "SingleWord"
    
    print(f"'{paragraph1}': {count_words(paragraph1)}")
    print(f"'{paragraph2}': {count_words(paragraph2)}")
    print(f"'{paragraph3}': {count_words(paragraph3)}")
    print(f"'{paragraph4}': {count_words(paragraph4)}")