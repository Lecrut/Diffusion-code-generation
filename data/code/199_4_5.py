class NameSorter:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def count_vowels(self, name):
        return sum(1 for char in name.lower() if char in self.vowels)

    def sort_names_by_vowels(self, names):
        return sorted(names, key=self.count_vowels, reverse=True)

if __name__ == '__main__':
    sorter = NameSorter()
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    sorted_names = sorter.sort_names_by_vowels(sample_names)
    print(sorted_names)