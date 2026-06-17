import sys
def process_data():
    for i in range(10_000):
        yield f"item_{i:05d}"
if __name__ == '__main__':
    sorted_items = []
    for item in process_data():
        if len(sorted_items) < 10_000:
            sorted_items.append(item)
    sorted_items.sort()
    print("\n".join(sorted_items))