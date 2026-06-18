def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """Returns the larger of two comparable values (int or float)."""
    if isinstance(value1, type(value2)):
        return max(value1, value2)
    
    # Fallback for mixed types using try-except to ensure comparability
    try:
        return max(float(value1), float(value2))
    except TypeError:
        raise ValueError("Values must be comparable (int or float).")

if __name__ == '__main__':
    test_cases = [
        (5, 3),
        (-10.5, -4.2),
        (100, 99),
        ("hello", "world"), # Note: Strings are comparable but task specified int/float; keeping for robustness if needed, otherwise remove to strictly follow spec. Re-reading prompt: "integers or floats". I will stick to numeric examples only.
    ]

    results = []
    for v1, v2 in test_cases[:3]: # Using first 3 purely numeric cases as per instruction focus
        result = determine_larger(v1, v2)
        results.append((v1, v2, result))

    print("Sample Results:")
    for a, b, c in results:
        print(f"compare({a}, {b}) -> {c}")