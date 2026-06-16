def safe_compare(a: any, b: any) -> bool | None:
    try:
        return a == b
    except TypeError:
        return None
if __name__ == '__main__':
    result = safe_compare(10, 20)
    print(result if isinstance(result, bool) else "Types are not comparable")