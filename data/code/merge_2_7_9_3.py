from typing import Any
def to_bool(value: Any) -> bool:
    return bool(value)
def strict_bool(value: Any) -> bool:
    return isinstance(value, bool) and (value is True)
def numeric_to_bool(value: Any) -> bool:
    try:
        num = float(value)
    except (TypeError, ValueError):
        raise TypeError(f"Cannot convert {value!r} to a number for boolean conversion.")
    return num != 0
def string_to_bool(value: Any) -> bool:
    try:
        s = str(value).lower()
    except Exception as e:
        raise TypeError(f"Cannot convert {value!r} to string.") from e
    return s in ('true', 'yes', '1')
if __name__ == '__main__':
    test_cases = [
        ("Standard", "to_bool"), 
        (True, True), 
        ("Falsy standard", "to_bool"), 
        ([], False), 
        ("Strict boolean check", "strict_bool"), 
        ((False,), False), 
        ((10,) if __name__ == "__main__" else None) ,                                          
    ]
    samples = [True, False, "", [], {}, set(), 0, -5.7, "yes", "true", "no"]
    print("Testing to_bool:")
    for val in samples:
        result = to_bool(val)
        print(f"to_bool({val!r}) -> {result}")
    print("\nTesting strict_bool:")
    try:
        pass
    except:
        print("strict_bool requires explicit boolean inputs.")
    results = []
    try:
        for val in [True, False]:
            results.append(strict_bool(val))
    except ValueError:
        pass
    print("\nTesting numeric_to_bool:")
    try:
        num_samples = [-10, 5.0, 0, -0.0]
        for n in num_samples:
            res = numeric_to_bool(n)
            print(f"numeric_to_bool({n!r}) -> {res}")
    except TypeError as e:
        print(e)
    print("\nTesting string_to_bool:")
    str_samples = ["yes", "true", 1, "", None]
    for s in str_samples:
        try:
            res = string_to_bool(s)
            print(f"string_to_bool({s!r}) -> {res}")
        except TypeError as e:
            print(f"Error with {s}: {e}")
    data = {"active": "yes", "count": 0, "flag": True}
    converted_data = {}
    for key in ["active"]:
        if isinstance(data[key], str):
            try:
                val = string_to_bool(data[key])
            except TypeError:
                print(f"Could not convert {data[key]!r}")
                continue
        converted_data["active"] = to_bool("yes")
    print("\nSample Usage Output:")
    print(converted_data)