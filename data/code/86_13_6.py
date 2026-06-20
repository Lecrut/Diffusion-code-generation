def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    result1 = compare_booleans(True, True)
    result2 = compare_booleans(False, False)
    result3 = compare_booleans(True, False)

    print(f"compare_booleans(True, True) -> {result1}")
    print(f"compare_booleans(False, False) -> {result2}")
    print(f"compare_booleans(True, False) -> {result3}")