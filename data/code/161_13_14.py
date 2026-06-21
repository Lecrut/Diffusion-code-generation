class SampleDataGenerator:
    SAMPLE_ITEMS = [
        {"id": 1, "name": "apple", "value": 42},
        {"id": 2, "name": "banana", "value": 99},
        {"id": 3, "name": "cherry", "value": 101},
        {"id": 4, "name": "date", "value": 55},
        {"id": 5, "name": "elderberry", "value": 200}
    ]

    @staticmethod
    def get_sample_list():
        return SampleDataGenerator.SAMPLE_ITEMS

if __name__ == '__main__':
    sample_list = SampleDataGenerator.get_sample_list()
    for item in sample_list:
        print(f"ID: {item['id']}, Name: {item['name']}, Value: {item['value']}")