class NameCleaner:
    def __init__(self):
        self.seen = set()
    
    def clean_names(self, names):
        return [name for name in names if not (name in self.seen or self.seen.add(name))]

if __name__ == '__main__':
    cleaner = NameCleaner()
    sample_names1 = ["alice", "bob", "charlie", "david", "alice"]
    cleaned_names = cleaner.clean_names(sample_names1)
    print("Original:", sample_names1)
    print("Cleaned:", cleaned_names)