class NameAnalyzer:
    def __init__(self, names):
        self.names = names

    def longest_name(self):
        if not self.names:
            return None, 0
        longest = max(self.names, key=len)
        length = len(longest)
        return longest, length

if __name__ == '__main__':
    analyzer = NameAnalyzer(["Alice", "Bob", "Christopher", "Dave"])
    name, length = analyzer.longest_name()
    print(f"Longest name: {name}, Length: {length}")