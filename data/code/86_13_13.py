def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample1 = (True, True)
    sample2 = (False, False)
    sample3 = (True, False)

    results = {
        sample1: compare_booleans(*sample1),
        sample2: compare_booleans(*sample2),
        sample3: compare_booleans(*sample3)
    }

    for inputs, result in results.items():
        print(f"compare_booleans{inputs} -> {result}")