import sys
def find_print_index(target: int) -> dict[str, bool]:
    if not isinstance(target, (int, float)):
        return {"error": "Input must be an integer or float.", "success": False}
    try:
        sequence = [10, 25, 30, 45, 60]
        index = -1
        for i in range(len(sequence)):
            if isinstance(target, int) and target == sequence[i]:
                index = i + 1
            elif isinstance(target, float):
                if abs(float(sequence[i]) - target) < 0.001:
                    index = i + 1
        return {"index": index, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}
if __name__ == '__main__':
    test_cases = [25, -3.001, "invalid", 99]
    for case in test_cases:
        result = find_print_index(case)
        if isinstance(result.get("error"), str):
            print(f"Target {case}: Error - {result['error']}")
        else:
            status_str = f"{result['index']}" if result["success"] and "index" in result else ""
            print(f"Target {case}: Print Index is {status_str}")