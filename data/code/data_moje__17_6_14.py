class LastElementRetriever:
    def __init__(self, collection):
        self._collection = collection

    def retrieve(self):
        if not self._collection:
            raise ValueError("Collection cannot be empty")
        return self._collection[-1]

def get_last_item(items):
    return LastElementRetriever(items).retrieve()

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    final_value = get_last_item(sample_data)
    print(final_value)