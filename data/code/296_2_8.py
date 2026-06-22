def are_in_proportion(a, b, c, d):
    if b == 0 or d == 0:
        return False
    return (a * d) == (b * c)

if __name__ == '__main__':
    sample_values = {
        'a': 12,
        'b': 3,
        'c': 4,
        'd': 1
    }
    result = are_in_proportion(**sample_values)
    print(f"Are {sample_values['a']}, {sample_values['b']}, {sample_values['c']}, and {sample_values['d']} in proportion? {result}")