import sys
def check_item_existence(items: list, target) -> bool:
    seen = set()
    for item in items:
        if item == target:
            return True
        seen.add(item)
    return False
if __name__ == '__main__':
    data = [10, 25, 'apple', None, 3.14]
    print(check_item_existence(data, 25))