def are_equivalent(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    for a, b in sample_values:
        print(are_equivalent(a, b))