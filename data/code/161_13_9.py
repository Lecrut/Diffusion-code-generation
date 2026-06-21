class SampleItemList:
    SAMPLE_DATA = [
        {"id": 1, "name": "apple", "quantity": 42},
        {"id": 2, "name": "banana", "quantity": 99},
        {"id": 3, "name": "cherry", "quantity": 101},
        {"id": 4, "name": "date", "quantity": 55},
        {"id": 5, "name": "elderberry", "quantity": 200}
    ]

    @staticmethod
    def get_sample_items():
        return SampleItemList.SAMPLE_DATA

if __name__ == '__main__':
    sample_items = SampleItemList.get_sample_items()
    print("Sample Item List:")
    for item in sample_items:
        print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}")