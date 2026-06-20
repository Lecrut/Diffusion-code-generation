class FlagValidator:
    def validate_exclusive_flags(self, flags):
        total = 0
        for flag in flags:
            if flag:
                total |= 1 << flags.index(flag)
        return total == (total & -total)

if __name__ == '__main__':
    validator = FlagValidator()
    test_cases = [
        ([0, 0, 0], True),
        ([1, 0, 0], True),
        ([0, 1, 0], True),
        ([1, 1, 0], False),
        ([1, 1, 1], False),
        ([0, 0], True),
        ([1], True),
        ([], True),
        ([1, 1], False)
    ]
    for flags in test_cases:
        print(validator.validate_exclusive_flags(flags))