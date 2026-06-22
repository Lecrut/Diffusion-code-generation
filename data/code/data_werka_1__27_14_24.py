from typing import Any

def are_different(var1: Any, var2: Any) -> bool:
    return var1 != var2

if __name__ == '__main__':
    sample1 = 42
    sample2 = '42'
    print(are_different(sample1, sample2))