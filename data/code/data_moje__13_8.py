from collections import defaultdict
from typing import Any, Callable, Dict, Tuple

def get_or_init_composite(
    dd: Dict[Tuple, Any],
    key: Tuple,
    factory: Callable[[], Any],
) -> Any:
    if key not in dd:
        dd[key] = factory()
    return dd[key]

if __name__ == '__main__':
    def make_list():
        return []

    composite_map: Dict[Tuple, list] = defaultdict(make_list)

    key1 = ('a', 1)
    key2 = ('b', 2)

    result1 = get_or_init_composite(composite_map, key1, make_list)
    result2 = get_or_init_composite(composite_map, key2, make_list)

    result1.append('value_for_a1')
    result2.append('value_for_b2')

    print(composite_map[key1])
    print(composite_map[key2])