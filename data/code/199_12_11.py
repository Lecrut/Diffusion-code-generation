class NameSorter:
    def __init__(self, names):
        self.names = list(set(names))

    def sort_names(self):
        sorted_names = sorted(self.names, key=str.lower)
        return sorted_names

if __name__ == '__main__':
    sample_names = ["alice", "bob", "Charlie", "david", "BOB"]
    sorter = NameSorter(sample_names)
    final_list = sorter.sort_names()
    print(final_list)