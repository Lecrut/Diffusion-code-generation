class Settings:
    DEFAULT_ITEMS = ["apple", "banana", "cherry"]
    @staticmethod
    def get_default_items():
        return Settings.DEFAULT_ITEMS
def process_data(items=None):
    if items is None:
        items = Settings.get_default_items()
    return items
if __name__ == '__main__':
    result1 = process_data()
    print(f"Result 1: {result1}")
    result2 = process_data(["orange", "grape"])
    print(f"Result 2: {result2}")