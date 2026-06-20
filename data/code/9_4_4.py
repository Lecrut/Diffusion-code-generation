def strip_whitespace(value):
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, bytes):
        return value.strip()
    if isinstance(value, list):
        return [item.strip() if isinstance(item, (str, bytes)) else item for item in value]
    if isinstance(value, tuple):
        return tuple(item.strip() if isinstance(item, (str, bytes)) else item for item in value)
    if isinstance(value, dict):
        return {k.strip() if isinstance(k, (str, bytes)) else k: v for k, v in value.items()}
    raise TypeError(f"Unsupported type: {type(value)}")

if __name__ == '__main__':
    result1 = strip_whitespace("  hello world  ")
    print(result1)
    result2 = strip_whitespace(["  a  ", "  b  "])
    print(result2)
    result3 = strip_whitespace({" key ": "value"})
    print(result3)
    result4 = strip_whitespace(b"  data  ")
    print(result4)
    result5 = strip_whitespace([1, "  str  ", 3])
    print(result5)