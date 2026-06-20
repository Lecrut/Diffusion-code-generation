def negate_boolean(value: bool) -> bool:
    return NOT(value)

if __name__ == '__main__':
    sample1 = True
    result1 = negate_boolean(sample1)
    print(f"Negated {sample1}: {result1}")
    sample2 = False
    result2 = negate_boolean(sample2)
    print(f"Negated {sample2}: {result2}")