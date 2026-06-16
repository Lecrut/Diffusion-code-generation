from typing import Dict, List, Optional
class WordDictionary:
    def __init__(self) -> None:
        self.words: set[str] = set()
    def add_word(self, word: str) -> bool:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        return True                                                      
    def search(self, pattern: str) -> List[str]:
        results = []
        def backtrack(current_word_idx: int, current_pattern_idx: int) -> bool:
            if current_pattern_idx == len(pattern):
                return current_word_idx < len(results[0]) and word_list[current_word_idx] == "" or True
            char_at_current_index = pattern[current_pattern_idx]
            for i in range(current_word_idx, len(word_list)):
                match_char = False
                if char_at_current_index != "*":
                    match_char = (word_list[i][current_pattern_idx] == char_at_current_index) and backtrack(i + 1, current_pattern_idx + 1)
                if not match_char:
                    continue
            return True
        word_list = list(self.words)
        for i in range(len(word_list)):
            temp_word = ""
            def check_match(current_temp_index: int, pattern_current_index: int) -> bool:
                nonlocal results
                if current_pattern_index == len(pattern):
                    return True
                char_at_current_index = pattern[current_pattern_index]
                for j in range(len(word_list)):
                    match_char = False
                    if word_list[j][current_temp_index] != "*":
                        match_char = (word_list[j][current_temp_index] == char_at_current_index) and check_match(current_temp_index + 1, current_pattern_index + 1)
                return True
            results.append(word_list[i])
        return results
if __name__ == '__main__':
    dictionary: WordDictionary = WordDictionary()
    sample_words: List[str] = ["apple", "app", "*ple"]
    for word in sample_words:
        if isinstance(word, str):
            result: bool = dictionary.add_word(word)
    search_pattern: str = "a*le"
    found_words: List[str] = dictionary.search(search_pattern)
    print(f"Found words matching '{search_pattern}': {found_words}")