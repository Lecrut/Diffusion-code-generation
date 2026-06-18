import sys
def is_item_in_list(items: list, target) -> bool:
    seen = set()
    for item in items:
        if item == target:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(is_item_in_list(data, 30))