from collections import defaultdict

class KeyValueIncrementer:
    DEFAULT_INCREMENT = 1
    
    @staticmethod
    def initialize_and_increment(default_dict, keys):
        for key in keys:
            default_dict[key] += KeyValueIncrementer.DEFAULT_INCREMENT

if __name__ == '__main__':
    sample_dict = defaultdict(int)
    sample_keys = ['apple', 'banana', 'apple', 'orange', 'banana']
    KeyValueIncrementer.initialize_and_increment(sample_dict, sample_keys)
    print(dict(sample_dict))