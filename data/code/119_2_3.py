from typing import Any

def reverse_order(a: Any, b: Any) -> tuple:
    return (b, a)

if __name__ == '__main__':
    print(reverse_order(1, 2))
    print(reverse_order('a', 'b'))
    print(reverse_order([1, 2], [3, 4]))