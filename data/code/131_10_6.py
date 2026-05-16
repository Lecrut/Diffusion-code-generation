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
        "System is running at high load",
        "Task requires medium attention",
        "Routine check complete",
        "Urgent error detected now",
        "Standard operation mode"
    ]
    results = []
    for data in sample_inputs:
        category = determine_category(data)
        results.append((data, category))
    for data, category in results:
        print(f"Input: {data}, Category: {category}")