from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not (a == b)

if __name__ == '__main__':
    sample_values = {
        'integers': (1, 2),
        'strings': ('hello', 'world'),
        'lists': ([1, 2, 3], [3, 4, 5]),
        'floats': (3.14, 3.140001),
        'booleans': (True, False)
    }
    
    for category, (val1, val2) in sample_values.items():
        print(f"are_different({val1}, {val2}) for {category}: {are_different(val1, val2)}")