class StringAnalyzer:
    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        self.s = s

    def length(self):
        return len(self.s)

if __name__ == '__main__':
    sample_string = "Innovative Solutions"
    analyzer = StringAnalyzer(sample_string)
    print(analyzer.length())