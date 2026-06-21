from collections import defaultdict

class KeyIncrementer:
    DEFAULT_INCREMENT = 1
    
    @staticmethod
    def initialize_and_increment(default_dict, keys):
        for key in keys:
            default_dict[key] += KeyIncrementer.DEFAULT_INCREMENT

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    KeyIncrementer.initialize_and_increment(sample_dict, sample_keys)
    print(dict(sample_dict))