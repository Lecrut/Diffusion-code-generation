import sys
def unique_values(iterable):
    seen = set()
    for item in iterable:
        if id(item) not in seen and isinstance(item, (list, tuple)):
            yield item
            seen.add(id(item))
        elif item not in seen:
            yield item
            seen.add(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b', 4, 5] * 2
    unique_result = list(unique_values(sample_list))
    print(f"Original length: {len(sample_list)}")
    print(f"Unique count: {len(unique_result)}")
    print("Result:", unique_result)