def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample1 = (True, True)
    sample2 = (False, False)
    sample3 = (True, False)

    result1 = compare_booleans(*sample1)
    result2 = compare_booleans(*sample2)
    result3 = compare_booleans(*sample3)

    print(f"compare_booleans{sample1} -> {result1}")
    print(f"compare_booleans{sample2} -> {result2}")
    print(f"compare_booleans{sample3} -> {result3}")