def analyze_logic(conditions):
    parsed_conditions = []
    for condition in conditions:
        try:
            parts = condition.split('if ')
            if len(parts) < 2:
                continue
            if_part = parts[0].strip()
            rest = parts[1].strip()
            if ' and ' in rest or ' or ' in rest:
                sub_conditions = [sub.strip() for sub in rest.split(' and ') if sub.strip()]
                if sub_conditions and ' or ' in rest:
                    logical_operator = 'or'
                    sub_conditions_list = [sub.strip() for sub in rest.split(' or ')]
                    if len(sub_conditions_list) > 1:
                        pass
                parsed_conditions.append({'if': if_part, 'then': rest})
            else:
                parsed_conditions.append({'if': if_part, 'then': rest})
        except Exception:
            continue
    return parsed_conditions
def check_contradictions(parsed_conditions):
    contradictions = []
    for i in range(len(parsed_conditions)):
        for j in range(i + 1, len(parsed_conditions)):
            cond1 = parsed_conditions[i]
            cond2 = parsed_conditions[j]
            if 'then' in cond1 and 'then' in cond2:
                if 'not' in cond1['then'] and cond1['then'].startswith('not '):
                    if cond1['if'] == cond2['if']:
                        contradictions.append(f"Potential contradiction found between '{cond1['if']}' and '{cond2['if']}'")
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30 then turn_on_ac and humidity < 70 if light_level is low then turn_off_lights if temperature > 30 then turn_on_fan"
    )
    conditions_data = analyze_logic(sample_string.split(' if '))
    contradictions = check_contradictions(conditions_data)
    if contradictions:
        print("Logical Contradictions Found:")
        for c in contradictions:
            print(f"- {c}")
    else:
        print("No obvious logical contradictions found based on simple string parsing.")