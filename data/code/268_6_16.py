import re

def extract_initial_word(sentence: str) -> str:
    if not sentence.strip():
        return ""
    match = re.match(r"(\S+)", sentence)
    return match.group(1) if match else ""

if __name__ == '__main__':
    sample_sentence_1 = "Hello world, this is a test."
    sample_sentence_2 = "  \t\n  Another line starts here."
    sample_sentence_3 = "123numbers and symbols"
    sample_sentence_4 = ""
    sample_sentence_5 = "   "
    
    print(f"Input: '{sample_sentence_1}' -> Initial Word: '{extract_initial_word(sample_sentence_1)}'")
    print(f"Input: '{sample_sentence_2}' -> Initial Word: '{extract_initial_word(sample_sentence_2)}'")
    print(f"Input: '{sample_sentence_3}' -> Initial Word: '{extract_initial_word(sample_sentence_3)}'")
    print(f"Input: '{sample_sentence_4}' -> Initial Word: '{extract_initial_word(sample_sentence_4)}'")
    print(f"Input: '{sample_sentence_5}' -> Initial Word: '{extract_initial_word(sample_sentence_5)}'")