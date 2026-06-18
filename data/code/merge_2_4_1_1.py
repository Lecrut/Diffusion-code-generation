import sys
def process_items(items: list) -> int:
    keep_count = 0
    for item in items:
        if isinstance(item, (int, float)) and item > 100:
            keep_count += 1
        elif isinstance(item, str):
            if len(item.strip()) >= 5:
                keep_count += 1
    return keep_count
if __name__ == '__main__':
    sample_data = [3.14, "hello", 200, "", None, "python"]
    result = process_items(sample_data)
    print(result)