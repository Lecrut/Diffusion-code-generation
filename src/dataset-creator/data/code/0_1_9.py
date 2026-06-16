def compare_values(a: any, b: any) -> bool | None:
    try:
        return a == b
    except TypeError:
        return None
if __name__ == '__main__':
    result = compare_values(10, 20)
    print(result if isinstance(result, bool) else "Types are not comparable")