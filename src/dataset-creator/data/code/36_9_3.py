from typing import Any, Dict, FrozenSet
def create_immutable_lookup_table(data: list[tuple[Any, ...]]) -> dict[FrozenSet[int], int]:
    result = {}
    for item in data:
        key_frozenset = frozenset(item)
        if key_frozenset not in result:
            result[key_frozenset] = len(result) + 1
    return result
if __name__ == '__main__':
    sample_data = [(1, 'a'), (2, 'b'), ('c', 3), (4, 'd')]
    lookup_table = create_immutable_lookup_table(sample_data)
    for key in lookup_table:
        assert isinstance(key, frozenset), "All keys must be frozensets"
    print(lookup_table)