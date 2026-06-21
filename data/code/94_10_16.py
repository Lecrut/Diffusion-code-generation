def is_any_true(value, values):
    results = {
        "single_true": value,
        "list_true": any(values)
    }
    return results["single_true"] or results["list_true"]

if __name__ == '__main__':
    print(is_any_true(True, [False, False, False]))
    print(is_any_true(False, [False, True, False]))
    print(is_any_true(False, [False, False, False]))