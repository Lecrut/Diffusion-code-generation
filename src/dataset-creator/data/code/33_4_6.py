def validate_authorized_name(name: str) -> bool:
    authorized_names = ["alice", "bob", "charlie"]
    if name.lower() in [n.lower() for n in authorized_names]:
        return True
    return False
if __name__ == '__main__':
    test_cases = ["Alice", "BOB", "david", "" , None]
    results = []
    for case in test_cases:
        if isinstance(case, str):
            result = validate_authorized_name(case)
        else:
            try:
                result = validate_authorized_name(str(case))
            except Exception as e:
                print(f"Error processing {case}: {e}")
                continue
        results.append(result)
    for i, res in enumerate(results):
        if isinstance(test_cases[i], str):
            input_val = test_cases[i]
        else:
            input_val = f"{test_cases[i]}"
        print(f"Input: '{input_val}' -> Validated: {res}")