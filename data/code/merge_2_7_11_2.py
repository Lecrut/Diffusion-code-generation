def parse_boolean_string(input_str: str) -> list[bool]:
    if not input_str.strip():
        return []
    try:
        values = [token for token in input_str.split()]
        result = []
        for val in values:
            normalized_val = str(val).strip().lower()
            if normalized_val in ('true', 'yes', 'on'):
                result.append(True)
            elif normalized_val in ('false', 'no', 'off'):
                result.append(False)
            else:
                try:
                    parsed_int = int(normalized_val)
                    if parsed_int == 1:
                        result.append(True)
                    elif parsed_int == 0:
                        result.append(False)
                    else:
                        raise ValueError(f"Invalid boolean representation '{normalized_val}'")
                except ValueError as e:
                    return [None] if len(result) == 0 else result + [None]
        return result
    except Exception:
        return []
if __name__ == '__main__':
    sample_input = "True False Yes No on off"
    output_result = parse_boolean_string(sample_input)
    print(output_result)