class NameManager:
    def __init__(self, names):
        self.names = list(set(names))
    def process_names(self):
        processed_names = []
        for name in self.names:
            title_cased_name = name.title()
            processed_names.append(title_cased_name)
        processed_names.sort()
        self.names = processed_names
        return self.names
if __name__ == '__main__':
    sample_names = ["alice", "bob", "Charlie", "alice", "david", "BOB"]
    manager = NameManager(sample_names)
    final_list = manager.process_names()
    print(final_list)