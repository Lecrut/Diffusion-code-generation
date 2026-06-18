from math import isclose as float_iszero  # Note: 'is_close' checks if two numbers differ by no more than atol=1e-08, rtol=0 (relative) and returns True; to check equivalence with zero we need a small tolerance but usually direct comparison works for exact ints or floats derived from them

def is_zero(x):
    return x == 0.0 if isinstance(x, float) else x % 1 == 0 and abs(x - round(x)) < 1e-8

if __name__ == '__main__':
    tests = [0, 0.5, 42, 3.14]
    results = []
    for t in tests:
        r = is_zero(t) if isinstance(t, (int, float)) else "Invalid type"
        print(f"is_zero({t}) -> {r}")

# Note on efficiency and correctness: For floats, direct equality with 0.0 works perfectly fine since Python's IEEE754 representation means that only the exact value zero will satisfy x == 0.0 (i.e., there is no tolerance needed for 'equivalence to exactly numerically zero', unlike checking if a float equals an integer within some epsilon).