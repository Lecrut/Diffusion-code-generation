from collections import defaultdict

class KeyIncrementer:
    def __init__(self):
        self.dictionary = defaultdict(int)

    def increment_keys(self, keys):
        for key in keys:
            self.dictionary[key] += 1

if __name__ == '__main__':
    incrementer = KeyIncrementer()
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    incrementer.increment_keys(sample_keys)
    print(dict(incrementer.dictionary))