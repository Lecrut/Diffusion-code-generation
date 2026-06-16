import operator as op
def safe_greater(a: any, b: any) -> bool | None:
    try:
        return op.gt(a, b)
    except TypeError:
        raise ValueError("Inputs must be numeric.") from None
    except AttributeError:
        raise TypeError("Operands do not support comparison.") from None
if __name__ == '__main__':
    result = safe_greater(10.5, 3)
    print(result if isinstance(result, bool) else "Error occurred")