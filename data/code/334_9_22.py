from typing import Tuple
def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    input_data = "hello world"
    words: Tuple[str, str] = tuple(input_data.split())
    result = combine_words(words[0], words[1])
    print(result)