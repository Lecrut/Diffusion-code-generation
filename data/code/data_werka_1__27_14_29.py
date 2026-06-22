from typing import Any

def are_different(var1: Any, var2: Any) -> bool:
    return var1 != var2

if __name__ == '__main__':
    sample_var1 = 42
    sample_var2 = "42"
    result = are_different(sample_var1, sample_var2)
    print(result)