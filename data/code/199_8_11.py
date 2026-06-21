from collections import Counter

class NameFrequencyCounter:
    def __init__(self, names):
        self.names = names
    
    def count_frequencies(self):
        return sorted(Counter(self.names).items(), key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    counter = NameFrequencyCounter(['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob'])
    result = counter.count_frequencies()
    print(result)