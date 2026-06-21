from collections import defaultdict
import json

def get_or_default(d: dict, key: tuple, factory):
    return d[key] if key in d else factory()

def main():
    d = defaultdict(int)
    composite_key = ("a", 1)
    val = get_or_default(d, composite_key, lambda: json.dumps({"status": "fresh"}))
    print(val)
    d[composite_key] = 42
    val2 = get_or_default(d, composite_key, lambda: json.dumps({"status": "fresh"}))
    print(val2)

if __name__ == '__main__':
    main()