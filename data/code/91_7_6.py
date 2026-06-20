def negate_boolean(boolean_list: list) -> bool:
    return not boolean_list[0]

if __name__ == '__main__':
    sample_true = [True]
    sample_false = [False]
    print(f"Negation of {sample_true}: {negate_boolean(sample_true)}")
    print(f"Negation of {sample_false}: {negate_boolean(sample_false)}")