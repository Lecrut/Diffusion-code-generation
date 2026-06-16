from dataclasses import dataclass
@dataclass(frozen=True)
class WordEntry:
    word: str
    definition: str
    part_of_speech: str
    example_sentence: str
if __name__ == '__main__':
    dictionary = {
        "Python": WordEntry(word="Python", definition="A high-level, interpreted programming language.", part_of_speech="noun", example_sentence="She learned Python for web development."),
        "Algorithm": WordEntry(word="Algorithm", definition="An ordered sequence of operations to solve a problem.", part_of_speech="noun", example_sentence="The sorting algorithm runs in O(n log n) time."),
    }
    print("Word Dictionary")
    print("-" * 30)
    for word_obj, entry in dictionary.items():
        print(f"\n{entry.word}")
        print(f"Definition: {entry.definition}")
        print(f"Part of Speech: {entry.part_of_speech}")
        print(f"Example: \"{entry.example_sentence}\"")