def convert_to_bool(literals):
    CONVERSION_MAP = {
        "True": True,
        "true": True,
        "TRUE": True,
        "False": False,
        "false": False,
        "FALSE": False,
    }
    return [CONVERSION_MAP[literal.strip()] if literal in CONVERSION_MAP else None for literal in literals]

if __name__ == '__main__':
    sample_values = ["True", "true", " FALSE ", "No"]
    result = convert_to_bool(sample_values)
    print(result)