import sys
def determine_category(input_data):
    if not input_data:
        return "UNKNOWN"
    data_str = str(input_data).lower()
    if "high" in data_str or "urgent" in data_str:
        return "PRIORITY"
    elif "medium" in data_str or "standard" in data_str:
        return "NORMAL"
    elif "low" in data_str or "minor" in data_str:
        return "LOW"
    else:
        return "OTHER"
if __name__ == '__main__':
    sample_inputs = [
        "High priority request",
        "Standard task",
        "Low importance item",
        "Urgent notification",
        "A regular update"
    ]
    for item in sample_inputs:
        result = determine_category(item)
        print(result)