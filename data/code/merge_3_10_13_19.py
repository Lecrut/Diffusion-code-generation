import sys

def parse_temperature(value: str) -> float | None:
    """Attempt to convert a string to a float."""
    try:
        return float(value.strip())
    except ValueError:
        return None

if __name__ == '__main__':
    temp_a = 25.0
    temp_b = -10.0

    if parse_temperature(str(temp_a)) is not None and \
       parse_temperature(str(temp_b)) is not None:
        t_a, t_b = float(temp_a), float(temp_b)
        
        result_lines = []
        if t_a > t_b:
            result_lines.append(f"{t_a}°C is greater than {t_b}°C")
        elif t_a < t_b:
            result_lines.append(f"{t_a}°C is less than {t_b}°C")
        else:
            result_lines.append(f"{t_a}°C equals {t_b}°C")

        print('\n'.join(result_lines))
    else:
        print("Error: Invalid temperature values provided.")