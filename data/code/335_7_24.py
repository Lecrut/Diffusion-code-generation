import re
def split_sentence(sentence: str) -> list[str]:
    words = sentence.split()
    return [word for word in words if len(word.strip()) > 0]
if __name__ == '__main__':
    sample_sentences = ["Hello world!", "Python is great.",   ""]
    results = []
    for s in sample_sentences:
        result = split_sentence(s)
        print(f"Input: '{s}' -> Output: {result}")