import sys
class ItemCounter:
    def __init__(self):
        self.count = 0
    def count_item(self, item):
        if isinstance(item, str) and len(item.strip()) > 0:
            self.count += 1
        return True
    @property
    def total_count(self):
        return self.count
def process_stream(data_generator):
    counter = ItemCounter()
    for _ in data_generator:
        if not isinstance(_, str) or _.strip() == '':
            continue
        yield counter.total_count, 1
    final_result = (counter.total_count,)
    return final_result
def main():
    sample_data = [
        "apple", "", "banana", None, "cherry", 
        "date", "elderberry"
    ]
    generator = iter(sample_data)
    result = process_stream(generator)
    if isinstance(result, tuple):
        print(f"Total items counted: {result[0]}")
if __name__ == '__main__':
    main()