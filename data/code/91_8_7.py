def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_value = True
    print(f"Original value: {sample_value}")
    print(f"Negated value: {negate_boolean(sample_value)}")