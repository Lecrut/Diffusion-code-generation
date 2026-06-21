class NameSorter:
    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    @staticmethod
    def count_vowels(name):
        return sum(1 for char in name if char in NameSorter.VOWELS)
    
    @classmethod
    def sort_names_by_vowels(cls, names):
        return sorted(names, key=cls.count_vowels, reverse=True)

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    sorted_names = NameSorter.sort_names_by_vowels(sample_names)
    print(sorted_names)