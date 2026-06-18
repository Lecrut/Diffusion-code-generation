import sys

def parse_temperature(value: str) -> float | None:
    """Attempt to convert a string input into a float temperature."""
    try:
        return float(value.strip())
    except ValueError:
        return None

def compare_temperatures(t1_str: str, t2_str: str) -> tuple[float | None, float | None]:
    """Parse and validate two temperature inputs. Returns (t1, t2)."""
    temp_1 = parse_temperature(t1_str)
    temp_2 = parse_temperature(t2_str)

    if not temp_1 or not temp_2:
        print("Error: Invalid numeric input provided.")
        return None, None  # Type ignored for clarity in flow control
    return temp_1, temp_2

if __name__ == '__main__':
    sample_t1 = "36.5"
    sample_t2 = "-10.0"

    t1_val: float | None
    t2_val: float | None
    result_msg = ""

    try:
        t1_val, t2_val = compare_temperatures(sample_t1, sample_t2)
        
        if t1_val is not None and t2_val is not None:
            comparison_result = {
                't1': t1_val,
                't2': t2_val,
                'higher_temp_label': "First",
                'lower_temp_label': "Second"
            }

            if t1_val == t2_val:
                result_msg = f"{comparison_result['t1']}°C is equal to {comparison_result['t2']}°C."
            elif comparison_result['higher_temp_label'] == "First":
                result_msg = f"{comparison_result['t1']}°C is higher than {comparison_result['lower_temp_label'].capitalize()} ({comparison_result['t2']}°C)."
            else:
                result_msg = f"{comparison_result['lower_temp_label'].capitalize()} ({comparison_result['t2']}°C) is lower than {comparison_result['higher_temp_label'].capitalize()} ({comparison_result['t1']}°C)."

        print(result_msg) if t1_val and t2_val else None
    except Exception:
        result_msg = "Error occurred during temperature comparison."
        print(result_msg)