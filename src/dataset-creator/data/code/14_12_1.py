from typing import Iterator, Iterable
def unique_values(iterable: Iterable) -> list:
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen:
            seen.add(id(item))
            result.append(item)
        return result
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(unique_values(sample_list))