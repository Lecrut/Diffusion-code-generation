class NameManager:
    def __init__(self, names):
        self.names = set(names)
    def process_names(self):
        processed_names = []
        for name in self.names:
            processed_name = name.title()
            processed_names.append(processed_name)
        self.names = set(processed_names)
        sorted_names = sorted(list(self.names))
        return sorted_names
if __name__ == '__main__':
    sample_names = ["alice", "bob", "Alice", "charlie", "bob", "diana", "ALICE"]
    manager = NameManager(sample_names)
    result = manager.process_names()
    print(result)