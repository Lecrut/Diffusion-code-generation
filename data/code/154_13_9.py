class FrequencyMapper:
    def __init__(self):
        self.DATA = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    
    @staticmethod
    def create_frequency_map(data):
        return {item: data.count(item) for item in set(data)}
    
if __name__ == '__main__':
    freq_mapper = FrequencyMapper()
    frequency_map = freq_mapper.create_frequency_map(freq_mapper.DATA)
    print(frequency_map)