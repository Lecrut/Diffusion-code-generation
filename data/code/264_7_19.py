import re

def group_words_by_length(text: str) -> dict[int, list[str]]:
    words = re.findall(r'\w+', text)
    word_lengths = {}
    
    for word in words:
        length = len(word)
        if length not in word_lengths:
            word_lengths[length] = []
        word_lengths[length].append(word)
    
    return word_lengths

if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, how are you?"
    sample_string_2 = "  Multiple   spaces\tand\nnewlines\nwith punctuation... "
    sample_string_3 = "Word123-with_hyphens and $symbols."
    
    print(f"Input: '{sample_string_1}'")
    result_1 = group_words_by_length(sample_string_1)
    print(f"Output: {result_1}\n")
    
    print(f"Input: '{sample_string_2}'")
    result_2 = group_words_by_length(sample_string_2)
    print(f"Output: {result_2}\n")