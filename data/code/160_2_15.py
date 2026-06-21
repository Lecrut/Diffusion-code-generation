class ItemFrequency:
    @staticmethod
    def calculate_frequency(item_list):
        freq = {}
        for item in item_list:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(ItemFrequency.calculate_frequency(sample_items))