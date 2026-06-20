def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    is_active = True
    assert isinstance(is_active, bool), "is_active must be a boolean"
    result = negate_boolean(is_active)
    print(result)