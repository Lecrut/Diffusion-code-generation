class NameProcessor:
    def __init__(self, names):
        self.names = names

    def longest_name(self):
        if not self.names:
            return None, 0
        longest = max(self.names, key=len)
        length = len(longest)
        return longest, length

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Christopher", "Dave"]
    processor = NameProcessor(sample_names)
    name, length = processor.longest_name()
    print(f"Longest name: {name}, Length: {length}")