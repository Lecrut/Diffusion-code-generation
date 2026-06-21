from collections import Counter

class NameFrequencyCounter:
    @staticmethod
    def count_frequency(names):
        return sorted(Counter(names).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob']
    result = NameFrequencyCounter.count_frequency(sample_names)
    print(result)