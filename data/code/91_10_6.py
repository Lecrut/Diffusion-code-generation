TRUE_MAPPING = {
    True: False,
    False: True
}

def get_negated_boolean(flag: bool) -> bool:
    return TRUE_MAPPING[flag]

if __name__ == '__main__':
    print(get_negated_boolean(True))
    print(get_negated_boolean(False))