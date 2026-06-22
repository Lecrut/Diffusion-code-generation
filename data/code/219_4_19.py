class MaxFinder:
    @staticmethod
    def find_max(dictionary):
        if not dictionary:
            return None, None
        max_key = max(dictionary, key=dictionary.get)
        max_value = dictionary[max_key]
        return max_key, max_value

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 1, 'e': 5, 'f': 9, 'g': 2}
    max_key, max_value = MaxFinder.find_max(sample_dict)
    print(f"Key: {max_key}, Value: {max_value}")