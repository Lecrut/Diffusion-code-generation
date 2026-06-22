class UppercaseDict:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def print_uppercase_pairs(self):
        for key, value in self.dictionary.items():
            print(f"{key.upper()}: {value.upper()}")

if __name__ == '__main__':
    sample_dict = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    uppercase_dict_instance = UppercaseDict(sample_dict)
    uppercase_dict_instance.print_uppercase_pairs()