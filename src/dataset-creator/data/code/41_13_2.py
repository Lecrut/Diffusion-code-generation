import sys
class StreamingCounter:
    def __init__(self):
        self.count = 0
    def count_item(self, item):
        if isinstance(item, str) and len(item.strip()) > 0:
            self.count += 1
        return True
    def get_count(self):
        return self.count
def generate_large_dataset():
    for i in range(1_000_000):
        yield f"Item_{i}"
if __name__ == '__main__':
    counter = StreamingCounter()
    items_to_process = generate_large_dataset()
    for item in items_to_process:
        if not isinstance(item, str):
            continue
        try:
            count_item_result = counter.count_item(item)
            if count_item_result is True:
                pass
        except Exception as e:
            print(f"Error processing {item}: {e}", file=sys.stderr)
    final_count = counter.get_count()
    print(f"Total items counted: {final_count}")