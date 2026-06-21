from collections import Counter

class ElementCounter:
    def __init__(self):
        self.counts = Counter()
    
    def add_elements(self, data):
        self.counts.update(data)
    
    def get_counts(self):
        return dict(self.counts)

if __name__ == '__main__':
    counter = ElementCounter()
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    counter.add_elements(sample_list)
    print(counter.get_counts())