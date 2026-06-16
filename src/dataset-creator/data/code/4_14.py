import sys
def parse_and_execute(data: dict) -> tuple[str, list]:
    log = []
    if "mode" not in data:
        return "ERROR", ["Missing 'mode' key"]
    mode = data["mode"].lower()
    valid_modes = {"process": True, "validate": False}
    if mode not in valid_modes:
        return f"ERROR: Invalid mode '{data['mode']}'", [f"Valid modes are {list(valid_modes.keys())}"]
    value = data.get("value", "")
    try:
        parsed_value = int(value) if "process" == mode else float(value)
        if not (parsed_value > 0):
            return f"ERROR: Value must be positive for '{mode}'", [f"Parsed {parsed_value} is non-positive"]
        log.append(f"Successfully executed in {mode.upper()} with value={value}")
    except ValueError as e:
        return f"ERROR: Invalid numeric format", [str(e)]
    if mode == "process":
        result = parsed_value * 2 + 10
        output_data = {"status": "success", "result": result, "mode": mode}
        log.append(f"Calculated result for {output_data}")
        return f"SUCCESS: Mode={mode}, Result={result}", [f"{log[-1]}"]
    elif mode == "validate":
        if parsed_value < 0.5 or parsed_value > 99.9:
            output_data = {"status": "failed", "reason": "out_of_range"}
            log.append(f"Validation failed for {output_data}")
            return f"VALIDATION_FAILED: Range [0.5, 99.9] exceeded", [f"{log[-1]}"]
        else:
            output_data = {"status": "passed", "score": parsed_value}
            log.append(f"Validation passed for {output_data}")
            return f"VALIDATION_PASSED: Score={parsed_value}", [f"{log[-1]}"]
def main():
    sample_input = {
        "mode": "process", 
        "value": "42.5"
    }
    status, logs = parse_and_execute(sample_input)
    print(f"\n=== EXECUTION STATUS: {status} ===")
    for log_entry in logs:
        print(log_entry)
if __name__ == '__main__':
    main()