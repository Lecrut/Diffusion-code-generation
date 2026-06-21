TRUTHY_CHECKS = {
    "empty": [],
    "all_false": [False, 0, None, "", []],
    "mixed": [0, False, None, 1],
    "all_truthy": [1, True, "a", [1]],
}

def has_any_truthy(iterable):
    return any(iterable)

if __name__ == '__main__':
    for name, values in TRUTHY_CHECKS.items():
        result = has_any_truthy(values)
        print(result)