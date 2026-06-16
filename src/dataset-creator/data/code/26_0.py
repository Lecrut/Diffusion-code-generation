from dataclasses import dataclass
@dataclass(frozen=True)
class WordEntry:
    word: str
    definition: str
    part_of_speech: str
    def __post_init__(self):
        if not self.word.strip():
            raise ValueError("Word cannot be empty.")
        if len(self.definition) == 0:
            raise ValueError("Definition cannot be empty.")
class WordDictionary:
    def __init__(self, entries: list[WordEntry]):
        self._entries = sorted(entries, key=lambda e: (e.word.lower(), e.part_of_speech))
    @property
    def count(self) -> int:
        return len(self._entries)
    def find_word(self, target: str) -> WordEntry | None:
        normalized_target = target.strip().lower()
        for entry in self._entries:
            if entry.word.lower() == normalized_target:
                return entry
        return None
    def get_definition(self, word: str) -> str | None:
        entry = self.find_word(word)
        return entry.definition if entry else None
if __name__ == '__main__':
    sample_entries = [
        WordEntry("python", "A high-level programming language.", "language"),
        WordEntry("algorithm", "An ordered sequence of steps to solve a problem.", "noun"),
        WordEntry("variable", "A storage location in memory that holds data.", "noun")
    ]
    dictionary = WordDictionary(sample_entries)
    print(f"Total words: {dictionary.count}")
    target_word = "algorithm"
    result_entry = dictionary.find_word(target_word)
    if result_entry:
        print(f"\nFound word: '{result_entry.word}'")
        print(f"Definition: {result_entry.definition}")
        print(f"Part of Speech: {result_entry.part_of_speech}")
        direct_def = dictionary.get_definition("python")
        print(f"\nDirect lookup for 'python': {direct_def}")
    else:
        print("\nWord not found.")