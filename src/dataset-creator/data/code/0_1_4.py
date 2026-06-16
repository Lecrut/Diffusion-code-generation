def safe_compare(a: any, b: any) -> bool | None:
    try:
        return a == b
    except TypeError:
        return False
if __name__ == '__main__':
    result = safe_compare(5, 5)
    print(result if result is not None else "Types are incompatible")