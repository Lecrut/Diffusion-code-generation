class NameSorter:
    @staticmethod
    def sort_names(names):
        return sorted(set(name.lower() for name in names))

if __name__ == '__main__':
    sample_names = ["alice", "bob", "Charlie", "alice", "david", "Bob"]
    sorted_names = NameSorter.sort_names(sample_names)
    print(sorted_names)