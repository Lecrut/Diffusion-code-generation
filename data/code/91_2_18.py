is_active = True

def negate_value(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    print(negate_value(is_active))