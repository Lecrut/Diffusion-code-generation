import sys
class StreamCounter:
    def __init__(self):
        self.count = 0
    def count_item(self, item):
        if item is not None:
            self.count += 1
        return self.count
def generate_large_stream():
    for i in range(1_000_000):
        yield f"item_{i}"
if __name__ == '__main__':
    counter = StreamCounter()
    for item in generate_large_stream():
        count_value = counter.count_item(item)
    print(f"Total items counted: {counter.count}")