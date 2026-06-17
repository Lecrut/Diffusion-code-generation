import sys
from typing import Any, List, Dict, Set, Tuple, FrozenSet
def count_elements(container: Any) -> int:
    return len(container)
if __name__ == '__main__':
    samples = {
        'list': [1, 2, 3],
        'tuple': (4, 5),
        'set': {6},
        'frozenset': frozenset({7}),
        'dict': {'a': 1, 'b': 2},
    }
    results = {}
    for container_type in samples:
        try:
            count = count_elements(samples[container_type])
            results[container_type] = {
                'type': type(samples[container_type]).__name__,
                'count': count,
                'method_used': 'len()'
            }
        except TypeError as e:
            results[container_type] = {'error': str(e)}
    output_str = "Results:\n" + "\n".join(
        f"{k}: {v}" 
        for k, v in sorted(results.items())
    )
    print(output_str)