class NameProcessor:
    def __init__(self, names):
        self.names = names

    def reverse_names(self):
        self.names = [name[::-1] for name in self.names]

    def sort_names(self):
        self.names.sort()

if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
    processor = NameProcessor(sample_list)
    
    print("Original List:", processor.names)
    processor.reverse_names()
    print("Reversed Names:", processor.names)
    processor.sort_names()
    print("Sorted Reversed Names:", processor.names)