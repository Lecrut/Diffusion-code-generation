from dataclasses import dataclass
from typing import Dict, List
@dataclass(frozen=True)
class WordEntry:
    word: str
    definition: str
    part_of_speech: str
class DictionaryManager:
    def __init__(self):
        self._entries: Dict[str, WordEntry] = {}
    def add_entry(self, entry: WordEntry) -> None:
        if not isinstance(entry.word, str) or len(entry.word.strip()) == 0:
            raise ValueError("Word must be a non-empty string.")
        self._entries[entry.word.lower()] = entry
    def get_definition(self, word: str) -> str | None:
        normalized_word = word.lower().strip()
        return self._entries.get(normalized_word).definition if normalized_word in self._entries else None
    def search_by_pos(self, part_of_speech: str) -> List[str]:
        matching_words = []
        for entry in self._values():
            if entry.part_of_speech.lower() == part_of_speech.lower():
                matching_words.append(entry.word)
        return sorted(matching_words)
    def _values(self):
        return list(self._entries.values())
if __name__ == '__main__':
    dictionary = DictionaryManager()
    sample_entries = [
        WordEntry(word="Python", definition="A high-level programming language.", part_of_speech="noun"),
        WordEntry(word="Recursion", definition="The process of calling a function within itself.", part_of_speech="noun"),
        WordEntry(word="Variable", definition="A storage location that holds data values.", part_of_speech="noun"),
    ]
    for entry in sample_entries:
        dictionary.add_entry(entry)
    print("Sample Entry:", dictionary.get_definition("python"))
    print("Recursion Definition:", dictionary.get_definition("recursion"))
    nouns = dictionary.search_by_pos("noun")
    print(f"Nouns found: {nouns}")