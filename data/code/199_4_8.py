class NameSorter:
    def __init__(self):
        self.vowel_counts = {
            'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
            'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1
        }

    def count_vowels(self, name):
        return sum(self.vowel_counts.get(char, 0) for char in name)

    def sort_names_by_vowels(self, names):
        return sorted(names, key=self.count_vowels, reverse=True)

if __name__ == '__main__':
    sorter = NameSorter()
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    sorted_names = sorter.sort_names_by_vowels(sample_names)
    print(sorted_names)