TRUE_RECORD = {"label": "True", "negation": False}
FALSE_RECORD = {"label": "False", "negation": True}

NEGATION_MAP = {
    True: TRUE_RECORD,
    False: FALSE_RECORD
}

def get_negation_info(value: bool) -> dict:
    if value not in NEGATION_MAP:
        raise ValueError("Unsupported input type")
    return NEGATION_MAP[value]

if __name__ == '__main__':
    for sample in [True, False]:
        result = get_negation_info(sample)
        print(f"Original: {sample}, Negated: {result['negation']}")