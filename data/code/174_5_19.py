from collections import defaultdict

class KeyIncrementer:
    def __init__(self):
        self.default_dict = defaultdict(int)

    def increment_keys(self, keys):
        for key in keys:
            self.default_dict[key] += 1

if __name__ == '__main__':
    key_incrementer = KeyIncrementer()
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    key_incrementer.increment_keys(sample_keys)
    print(dict(key_incrementer.default_dict))