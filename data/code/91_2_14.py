is_active = True

def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample1 = False
    result1 = negate_boolean(sample1)
    print(f"Negation of {sample1}: {result1}")
    sample2 = is_active
    result2 = negate_boolean(sample2)
    print(f"Negation of {sample2}: {result2}")