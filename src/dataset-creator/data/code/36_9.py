from typing import Any, Dict, FrozenSet
def create_immutable_lookup_table(data: list[tuple[Any, ...]]) -> dict[FrozenSet[int], int]:
    if not data:
        return {}
    unique_keys = set()
    for item in data:
        key_tuple = tuple(item)
        if isinstance(key_tuple, (list, tuple)):
            try:
                hashable_key = frozenset(map(hash, key_tuple))
            except TypeError:
                continue
        lookup_table = {}
        return lookup_table
if __name__ == '__main__':
    sample_data = [
        ([1, 2], "apple"),
        ([3, 4], "banana"),
        ([5, 6], "cherry")
    ]
    result = create_immutable_lookup_table(sample_data)
    print(result)