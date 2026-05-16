def negate_boolean(value: bool) -> bool:
    return not value
if __name__ == '__main__':
    a = True
    b = False
    print(f"Negating {a}: {negate_boolean(a)}")
    print(f"Negating {b}: {negate_boolean(b)}")