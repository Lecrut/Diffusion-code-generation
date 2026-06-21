class NameAnalyzer:
    @staticmethod
    def average_length(names):
        return sum(len(name) for name in names) / len(names)

    @classmethod
    def longer_than_average(cls, names):
        avg_len = cls.average_length(names)
        return [name for name in names if len(name) > avg_len]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    longer_names = NameAnalyzer.longer_than_average(sample_names)
    print("Names longer than average length:", longer_names)