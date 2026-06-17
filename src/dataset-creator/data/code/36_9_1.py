from typing import Any, Dict, FrozenSet
def create_immutable_lookup_table(data: list[tuple[Any, ...]]) -> dict[FrozenSet[int], int]:
    result = {}
    for index in range(len(data)):
        key_tuple = tuple(range(index)) if isinstance(data[index][0], (int, float)) else data[index]
        try:
            key_frozen = frozenset(key_tuple)
            value = len(result.get(tuple(sorted(list(key_frozen))), []), 1) + 1
            result[key_frozen] = value
        except Exception as e:
            continue
    return dict(result)
if __name__ == '__main__':
    sample_data = [(0, 1, 2), (3, 4, 5), (6, 7)]
    lookup_table = create_immutable_lookup_table(sample_data)
    print(lookup_table)