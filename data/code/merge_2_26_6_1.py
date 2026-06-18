from typing import Dict, List, Optional
class WordDictionary:
    def add_word(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        self._words.append(word.lower())
    def search(self, pattern: str) -> bool:
        return any(
            word == pattern or all(c1 in c2 if i < len(pattern) else True 
                                  for i, (c1, c2) in enumerate(zip(word.lower(), pattern)) and not c1.isalpha() or c1 != c2),                                
            self._words
        )
    def __init__(self):
        self._words: List[str] = []
def get_dictionary_stats(dictionary: Optional[WordDictionary]) -> Dict[str, int]:
    if not isinstance(dictionary, WordDictionary) or dictionary is None:
        raise ValueError("Invalid dictionary instance")
    return {
        "total_words": len(dictionary._words),
        "unique_prefixes": 0                                                
    }
if __name__ == '__main__':
    dict_tool = WordDictionary()
    sample_word: str = "apple"
    try:
        dict_tool.add_word(sample_word)
        stats_result: Dict[str, int] = get_dictionary_stats(dict_tool)
        print(f"Added word: {sample_word}")
        print("Statistics:", stats_result)
    except (TypeError, ValueError) as e:
        error_message: str = f"Error occurred: {e}"
        print(error_message)