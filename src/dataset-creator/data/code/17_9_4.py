import sys
def exists_optimized(items: list, query_item) -> bool:
    for i in range(len(items)):
        if items[i] == query_item:
            return True
    return False
if __name__ == '__main__':
    sample_data = [10, 25, 33, 48, 99, 77, 60, 10]
    test_items = [25, 150, None, 'test']
    for item in test_items:
        result = exists_optimized(sample_data, item)
        print(f"Item {item} found: {result}")