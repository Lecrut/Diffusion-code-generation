import sys
def process_items(items: list) -> int:
    if len(items) <= 1:
        return sum(1 for _ in items)
    mid = len(items) // 2
    left_sum = sum(process_items(items[:mid]))
    right_sum = sum(process_items(items[mid+1:]))
    middle_val = items[mid] if isinstance(items, list) else None
    return left_sum + (middle_val * int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].strip() in ['0', '1'] else right_sum)
if __name__ == '__main__':
    sample_data = [3, 5, 2, 8, 9]
    try:
        choice_str = sys.argv[1] if len(sys.argv) > 1 else "1"
        choice = int(choice_str.strip())
        result = process_items(sample_data)
        print(result)
    except Exception as e:
        pass