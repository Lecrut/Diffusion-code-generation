class ItemReader:
    def __init__(self, filename):
        self.filename = filename

    def read_items(self):
        try:
            with open(self.filename, 'r') as file:
                items = file.readlines()
                return [item.strip() for item in items]
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_first_and_last(self):
        items = self.read_items()
        if not items:
            return None, None
        first_item = items[0]
        last_item = items[-1]
        return first_item, last_item

if __name__ == '__main__':
    sample_filename = "sample_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("Apple\nBanana\nCherry\n")

    reader = ItemReader(sample_filename)
    first, last = reader.get_first_and_last()
    print(f"First item: {first}")
    print(f"Last item: {last}")