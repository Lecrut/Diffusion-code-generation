import sys
def build_dict(iterable):
    result = {}
    for item in iterable:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k_type = type(key).__name__
                v_type = type(value).__name__
                if not isinstance(k_type, str):
                    raise TypeError(f"Unsupported key type {k_type}")
                result[key] = value
            except Exception:
                print(f"Skipping invalid entry with types ({key}, {value})", file=sys.stderr)
        else:
            try:
                key = item
                result[key] = None
            except Exception:
                print(f"Skipping invalid entry {item}", file=sys.stderr)
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "red"),
        (1, 2),
        ("banana", "yellow"),
        None,                            
        ["list_item"],                     
        ("cherry", "green")
    ]
    constructed_dict = build_dict(sample_data)
    print("Constructed Dictionary:")
    for k, v in constructed_dict.items():
        if isinstance(k, str):
            print(f'"{k}": "{v}"')
        else:
            print(f'{k}: {v}')