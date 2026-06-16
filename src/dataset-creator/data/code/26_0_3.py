from dataclasses import dataclass
@dataclass(frozen=True)
class WordEntry:
    word: str
    definition: str
    part_of_speech: str
    def __post_init__(self):
        if not self.word.strip():
            raise ValueError("Word cannot be empty.")
        words = [w for w in self.word.split() if w]
        if len(words) != 1 or any(not w.strip() for w in words):
            raise ValueError(f"Invalid word format: {self.word}")
if __name__ == '__main__':
    dictionary_data = [
        ("Python", "A high-level, interpreted programming language.", "noun"),
        ("Algorithm", "An ordered sequence of steps to solve a problem.", "noun"),
        ("Recursion", "The process where a function calls itself during execution.", "noun")
    ]
    entries: list[WordEntry] = []
    for word_data in dictionary_data:
        try:
            entry = WordEntry(word=word_data[0], definition=word_data[1], part_of_speech=word_data[2])
            entries.append(entry)
        except ValueError as e:
            print(f"Error creating entry for '{word_data[0]}': {e}")
    if not entries:
        print("No valid words added to dictionary.")
    else:
        print("\nDictionary Contents:")
        for idx, entry in enumerate(entries):
            print(f"{idx + 1}. Word: {entry.word}, Definition: '{entry.definition}', Part of Speech: {entry.part_of_speech}")