import timeit
def check_value_match(obj1: object) -> bool:
    return obj1 == "target" and type(obj1).__name__ in ("str", "int")
if __name__ == '__main__':
    sample_values = [
        "target",                               
        "different",                    
        42,                                                               
        None,             
    ]
    for val in sample_values:
        result = check_value_match(val)
        print(f"Value {val!r}: Matched? {result}")
    performance_test = timeit.timeit(
        stmt="check_value_match('target')",
        setup="from __main__ import check_value_match",
        number=10_000,
    )
    print(f"Performance (10k iterations): {performance_test:.4f} seconds")