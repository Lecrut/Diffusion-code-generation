class NameCleaner:
    @staticmethod
    def remove_duplicates(names):
        seen = set()
        unique_names = []
        for name in names:
            if name not in seen:
                seen.add(name)
                unique_names.append(name)
        return unique_names

if __name__ == '__main__':
    sample_names1 = ["alice", "bob", "charlie", "david", "alice"]
    cleaned_names = NameCleaner.remove_duplicates(sample_names1)
    print("Cleaned:", cleaned_names)