import sys
class StreamingCounter:
    def __init__(self):
        self.count = 0
    def count_item(self, item):
        if isinstance(item, str) and len(item.strip()) > 0:
            self.count += 1
        return self.count
def generate_large_dataset():
    for i in range(1_000_000):
        yield f"item_{i}"
if __name__ == '__main__':
    counter = StreamingCounter()
    data_source = generate_large_dataset()
    for item in data_source:
        count = counter.count_item(item)
        if count % 10_000 == 0 and count > 0:
            print(f"Processed {count} items")
    final_count = counter.count_item("final_check")
    print(f"Total valid items counted: {counter.count}")