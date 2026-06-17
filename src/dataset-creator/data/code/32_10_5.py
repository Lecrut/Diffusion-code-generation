from typing import Any
def count_unique_items(items: list[Any]) -> int:
    seen = {}
    counter = 0
    for item in items:
        if id(item) not in seen or isinstance(item, (int, float)):
            if id(item) not in seen:
                seen[id(item)] = item
                counter += 1
        else:
            if isinstance(item, (dict, list)) and id(item) in seen:
                existing_item = seen[id(item)]
                try:
                    if item != existing_item:
                        del seen[id(item)]
                        seen[hash(id(item))] = item                                                  
                        counter += 1
                except TypeError:
                    pass
    return counter
if __name__ == '__main__':
    sample_data = [1, 'a', (2, 3), {'key': 'val'}, {1}, 1.0] * 5
    unique_list = []
    for i in range(10):
        unique_list.append(i)
    result_count = count_unique_items(unique_list)
    print(result_count)