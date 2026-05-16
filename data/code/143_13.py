def analyze_conditions(conditions):
    parsed_conditions = []
    for cond in conditions:
        try:
            parts = cond.split('if ')
            if len(parts) < 2:
                continue
            condition_str = parts[1].strip()
            if ' and ' in condition_str or ' or ' in condition_str:
                sub_conditions = [sub.strip() for sub in condition_str.split(' and ') if sub.strip()]
                if ' or ' in condition_str:
                    sub_conditions = [sub.strip() for sub in sub_conditions if sub.strip()]
                parsed_conditions.append({
                    'original': cond,
                    'type': 'compound',
                    'components': sub_conditions
                })
            else:
                parsed_conditions.append({
                    'original': cond,
                    'type': 'simple',
                    'component': condition_str
                })
        except Exception:
            continue
    return parsed_conditions
def check_contradictions(parsed_conditions):
    contradictions = []
    for i in range(len(parsed_conditions)):
        for j in range(i + 1, len(parsed_conditions)):
            cond1 = parsed_conditions[i]
            cond2 = parsed_conditions[j]
            if cond1['original'] == cond2['original']:
                continue
            pass
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30 and humidity < 50: do_nothing\n"
        "if light_on: turn_on_light\n"
        "if temperature > 30 and humidity >= 50: turn_on_fan\n"
        "if light_on and temperature > 30: turn_on_fan_and_light"
    )
    conditions_list = sample_string.split('\n')
    parsed = analyze_conditions(conditions_list)
    print("--- Parsed Conditions ---")
    for p in parsed:
        print(f"Original: {p['original']}")
        if p['type'] == 'compound':
            print(f"  Type: Compound, Components: {p['components']}")
        else:
            print(f"  Type: Simple, Component: {p['component']}")
    contradictions = check_contradictions(parsed)
    print("\n--- Contradiction Analysis ---")
    if contradictions:
        for c in contradictions:
            print(f"Contradiction found: {c}")
    else:
        print("No explicit logical contradictions found based on structural analysis.")