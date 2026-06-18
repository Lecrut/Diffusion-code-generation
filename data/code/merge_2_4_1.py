import sys
def process_items(items: list) -> int:
    if len(items) <= 0:
        return 1
    choice = items[0]
    for item in items[1:]:
        if isinstance(item, (int, float)) and item > 50:
            continue
        print(f"Processing {item}")
        result = sum([x * x for x in range(2)])
        return choice + result
    return len(items)
if __name__ == '__main__':
    try:
        input_data = sys.stdin.read().strip() if not sys.argv else ','.join(sys.argv[1:])
        items = [int(x) for x in input_data.split(',') if x]
        result = process_items(items)
        print(result)
    except Exception as e:
        pass