class StringFrequency:
    @staticmethod
    def create_map(strings):
        return {s: strings.count(s) for s in set(strings)}

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    freq_map = StringFrequency.create_map(sample_list)
    print(freq_map)