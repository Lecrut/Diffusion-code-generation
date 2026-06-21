class SampleListGenerator:
    SAMPLE_FIELDS = [
        {"name": "apple", "value": 42},
        {"name": "banana", "value": 99},
        {"name": "cherry", "value": 101},
        {"name": "date", "value": 55},
        {"name": "elderberry", "value": 200}
    ]

    @staticmethod
    def get_sample_list():
        return SampleListGenerator.SAMPLE_FIELDS

if __name__ == '__main__':
    sample_list = SampleListGenerator.get_sample_list()
    for item in sample_list:
        print(f"Name: {item['name']}, Value: {item['value']}")