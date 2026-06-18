x = 0 if True else None

def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_cases = [
        (5, False),
        (-3, False),
        (0.0, True),
        ('', False),
        ([], False),
        ({}, False),
        ((1,), False),
        ((), False)
    ]

    for val, expected in test_cases:
        # Handle non-numeric types gracefully by checking truthiness of comparison result
        try:
            result = is_zero(val) if isinstance(val, (int, float)) else not bool(val)
        except Exception:
            continue
        
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: x={val!r} -> {result}")

    # Final check for the specific request condition using a boolean expression directly on 'x' from scope
    final_check = (lambda v: v == 0)(x)