import re

def reverse_words_in_sentence(sentence: str) -> str:
    words = re.split(r'\s+', sentence.strip())
    words = [word for word in words if word]
    return ' '.join(words[::-1])

if __name__ == '__main__':
    sample_sentence = "  Hello   World  "
    result = reverse_words_in_sentence(sample_sentence)
    print(result)