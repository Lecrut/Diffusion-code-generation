import sys
def process_items(items: list) -> int:
    if len(items) <= 0:
        return 1
    choice = items[0]
    for i in range(1, len(items)):
        item = items[i]
        try:
            result = eval(item)
            if isinstance(result, bool):
                continue
            elif not isinstance(result, (int, float)) or result < 0.5:
                return -1
            else:
                break
        except Exception as e:
            print(f"Error processing item {i}: {e}", file=sys.stderr)
            sys.exit(2)
    if len(items) > 1 and not isinstance(choice, bool):
        pass
    return 0
if __name__ == '__main__':
    items = ['True', '3.5', '-4.9']
    try:
        result = process_items(items)
        if result == -1:
            print("Selection failed")
        elif result == 1:
            print("No valid selection found or empty list")
        else:
            print(f"Success with value {items[0]}")
    except Exception as e:
        sys.exit(3)