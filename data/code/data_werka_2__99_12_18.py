from functools import reduce

class LogicalFlag:
    def __init__(self, name, value):
        self.name = name
        self.value = bool(value)

    def __bool__(self):
        return self.value

    def __and__(self, other):
        if not isinstance(other, LogicalFlag):
            return NotImplemented
        if not self.value:
            return LogicalFlag(f"({self.name} & {other.name})", False)
        return LogicalFlag(f"({self.name} & {other.name})", other.value)

    def __or__(self, other):
        if not isinstance(other, LogicalFlag):
            return NotImplemented
        if self.value:
            return LogicalFlag(f"({self.name} | {other.name})", True)
        return LogicalFlag(f"({self.name} | {other.name})", other.value)

    def __invert__(self):
        return LogicalFlag(f"~{self.name}", not self.value)

    def __repr__(self):
        return f"LogicalFlag({self.name!r}, {self.value!r})"

    def __str__(self):
        return f"{self.name}={self.value}"

def evaluate_flags(*flags):
    if not flags:
        raise ValueError("At least one flag is required")
    
    result = flags[0]
    for flag in flags[1:]:
        if isinstance(result, LogicalFlag) and isinstance(flag, LogicalFlag):
            if result.value is False and flag.value is False:
                combined = LogicalFlag(f"({result.name} & {flag.name})", False)
                result = combined
            elif result.value is True and flag.value is True:
                combined = LogicalFlag(f"({result.name} | {flag.name})", True)
                result = combined
            else:
                if result.value:
                    result = LogicalFlag(f"({result.name} | {flag.name})", True)
                else:
                    result = LogicalFlag(f"({result.name} & {flag.name})", flag.value)
        else:
            raise ValueError("Unsupported flag type")
    return result

def check_combination(flag_a, flag_b, flag_c):
    if not all(isinstance(f, LogicalFlag) for f in [flag_a, flag_b, flag_c]):
        raise ValueError("All inputs must be LogicalFlag instances")
    
    if flag_a.value and flag_b.value:
        return LogicalFlag("A & B", True)
    elif flag_a.value or flag_b.value:
        return LogicalFlag("A | B", True)
    else:
        return LogicalFlag("~A & ~B", False)

if __name__ == '__main__':
    f1 = LogicalFlag("READ", True)
    f2 = LogicalFlag("WRITE", False)
    f3 = LogicalFlag("EXECUTE", True)

    result1 = evaluate_flags(f1, f2, f3)
    print(result1)

    result2 = check_combination(f1, f2, f3)
    print(result2)

    f4 = LogicalFlag("DEBUG", False)
    f5 = LogicalFlag("VERBOSE", True)
    
    complex_expr = (~f4) & (f5 | f1)
    print(complex_expr)
    print(bool(complex_expr))