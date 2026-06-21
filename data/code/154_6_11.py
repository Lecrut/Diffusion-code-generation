class ItemFrequency:
    @staticmethod
    def count_frequencies(input_list):
        return [(item, input_list.count(item)) for item in set(input_list)]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    frequencies = ItemFrequency.count_frequencies(sample_list)
    print(frequencies)