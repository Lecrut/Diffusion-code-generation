import json
def validate_and_process(value: float) -> str:
    if value < 0:
        return "Value is negative."
    elif value <= 10:
        result = f"Small value {value} rounded to nearest integer: {round(value)}"
    else:
        data = {"input": value, "status": "processed", "type": "large"}
        result = json.dumps(data)
    return result
def run_operations():
    samples = [5.234, -10.5, 150.789]
    for val in samples:
        output = validate_and_process(val)
        print(f"Input: {val} -> Output: {output}")
if __name__ == '__main__':
    run_operations()