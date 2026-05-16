import sys
def categorize_input(data):
    if not data:
        return "No Data"
    if isinstance(data, str):
        data = data.lower().strip()
    if "error" in data or "fail" in data:
        return "Error Category"
    elif "high" in data or "urgent" in data:
        return "High Priority"
    elif "medium" in data or "standard" in data:
        return "Medium Priority"
    elif "low" in data or "routine" in data:
        return "Low Priority"
    else:
        return "Default Category"
if __name__ == '__main__':
    sample_inputs = [
        "System is running high load",
        "Routine check complete",
        "Error detected in module X",
        "Standard operation",
        "Low resource usage",
        "Urgent system alert"
    ]
    results = []
    for item in sample_inputs:
        category = categorize_input(item)
        results.append((item, category))
    for original, category in results:
        print(f"Input: {original}, Category: {category}")