import sys
def determine_category(input_data):
    if not input_data:
        return "Unknown"
    data_str = str(input_data).lower().strip()
    if "high" in data_str or "urgent" in data_str:
        return "Priority_High"
    elif "medium" in data_str or "standard" in data_str:
        return "Priority_Medium"
    elif "low" in data_str or "routine" in data_str:
        return "Priority_Low"
    else:
        return "Priority_Unknown"
if __name__ == '__main__':
    sample_inputs = [
        "High priority task",
        "Standard request",
        "Routine check",
        "Urgent system alert",
        "Low level notification",
        "Some random text"
    ]
    results = []
    for item in sample_inputs:
        category = determine_category(item)
        results.append((item, category))
    for original, category in results:
        print(f"Input: {original}, Category: {category}")