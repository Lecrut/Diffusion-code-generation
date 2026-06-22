from collections import defaultdict
from typing import Any, Callable, Dict, Tuple

def get_composite_value(data: Dict[Tuple, Any], key: Tuple, factory: Callable[[], Any]) -> Any:
    if key not in data:
        data[key] = factory()
    return data[key]

if __name__ == '__main__':
    d: defaultdict = defaultdict(list)
    result = get_composite_value(d, ('a', 'b'), list)
    result.append(1)
    result.append(2)
    second_result = get_composite_value(d, ('a', 'b'), list)
    print(second_result)