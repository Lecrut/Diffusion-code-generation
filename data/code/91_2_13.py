is_active = True

def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    result = negate_boolean(is_active)
    print(f"Negation of {is_active}: {result}")