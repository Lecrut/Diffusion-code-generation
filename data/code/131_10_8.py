import sys
def categorize_input(data):
    category = "Unknown"
    if not data:
        return category
    if isinstance(data, str):
        lower_data = data.lower().strip()
        if "error" in lower_data or "fail" in lower_data:
            category = "Error"
        elif "urgent" in lower_data or "critical" in lower_data:
            category = "High Priority"
        elif "request" in lower_data or "query" in lower_data:
            category = "Information Request"
        else:
            category = "General"
    elif isinstance(data, int):
        if data > 100:
            category = "Large Value"
        else:
            category = "Small Value"
    elif isinstance(data, list):
        if len(data) > 5:
            category = "Long List"
        else:
            category = "Short List"
    else:
        category = "Invalid Type"
    return category
if __name__ == '__main__':
    sample_inputs = [
        "System error occurred",
        "Please provide a query",
        150,
        ["a", "b", "c", "d", "e", "f"],
        "Urgent task",
        10,
        []
    ]
    results = []
    for item in sample_inputs:
        results.append(categorize_input(item))
    for result in results:
        print(result)