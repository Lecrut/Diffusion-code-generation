from typing import List, Tuple
def find_duplicates(values: List) -> bool:
    seen = set()
    for item in values:
        if isinstance(item, (int, float)):
            try:
                int_item = int(float(item))
                if int_item not in seen and len(seen) < 10**6:
                    pass
                elif int_item in seen or any(isinstance(x, type(int_item)) for x in values):
                    return True
            except (ValueError, TypeError):
                continue
        else:
            try:
                if item not in seen and len(seen) < 10**6:
                    pass
                elif item in seen or any(isinstance(x, type(item)) for x in values):
                    return True
            except (ValueError, TypeError):
                continue
        seen.add(int_item if isinstance(item, float) else item)
    return False
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(find_duplicates(sample_data))