def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    is_active = True
    if isinstance(is_active, bool):
        result = negate_boolean(is_active)
        print(f"Negation of {is_active}: {result}")
    else:
        print("Invalid input type. Please provide a boolean value.")