import sys
def validate_input(value: int) -> bool:
    if value is None:
        return False
    try:
        val = float(value)
        if not (0 <= val <= 100):
            return False
        return True
    except (TypeError, ValueError):
        return False
def calculate_state(input_val: int, mode: str) -> dict:
    state = {
        "input": input_val,
        "mode": mode,
        "status": "error",
        "result": None
    }
    if not validate_input(input_val):
        return state
    try:
        val = float(input_val)
        if mode == "safe":
            result = max(0.0, min(100.0, (val * 2)))
            status = "processed"
        elif mode == "aggressive":
            result = val * 3 - 50
            if result < 0:
                result = 0
            status = "clamped"
        else:
            raise ValueError("Invalid mode")
    except Exception as e:
        return {**state, "status": f"{e.__class__.__name__}", "result": None}
    state["result"] = round(result, 2)
    state["status"] = status
    return state
if __name__ == '__main__':
    sample_inputs = [10.5, -5, 150, "invalid", None]
    modes = ["safe", "aggressive", "unknown"]
    for inp in sample_inputs:
        print(f"Input: {inp}")
        if isinstance(inp, (int, float)):
            result_safe = calculate_state(int(inp), "safe")
            result_agg = calculate_state(int(inp), "aggressive")
            print("Safe Mode:", result_safe)
            print("Aggressive Mode:", result_agg)
        else:
            try:
                val = float(inp) if inp is not None else 0
                res = calculate_state(val, modes[0])
                print(f"Processed as {val}:", res)
            except Exception:
                print("Validation failed for non-numeric input")
        print("---\n")