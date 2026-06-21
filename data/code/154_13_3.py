class FrequencyMap:
    def __init__(self, data):
        self.data = data
        self.map = {item: data.count(item) for item in set(data)}

    def get_frequency(self, item):
        return self.map.get(item, 0)

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    freq_map_instance = FrequencyMap(sample_list)
    print(freq_map_instance.get_frequency('apple'))
    print(freq_map_instance.get_frequency('banana'))
    print(freq_map_instance.get_frequency('orange'))
    print(freq_map_instance.get_frequency('grape'))