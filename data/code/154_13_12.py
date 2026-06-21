class FrequencyMapper:
    @staticmethod
    def create_frequency_map(data):
        return {item: data.count(item) for item in set(data)}

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    frequency_map = FrequencyMapper.create_frequency_map(sample_list)
    print(frequency_map)