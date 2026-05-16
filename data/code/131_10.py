import sys
def categorize_input(data):
    if not data:
        return "Unknown"
    if isinstance(data, str):
        lower_data = data.lower().strip()
        if "error" in lower_data or "fail" in lower_data:
            return "Error Category"
        elif "urgent" in lower_data or "critical" in lower_data:
            return "High Priority"
        elif "request" in lower_data or "query" in lower_data:
            return "Information Request"
        else:
            return "General"
    if isinstance(data, int):
        if data > 100:
            return "Large Value"
        elif data > 0:
            return "Positive Value"
        else:
            return "Zero or Negative"
    if isinstance(data, list):
        if not data:
            return "Empty List"
        if all(isinstance(item, str) for item in data):
            return "String List"
        return "Mixed List"
    return "Uncategorized"
if __name__ == '__main__':
    sample_inputs = [
        "This is an urgent request for data.",
        "System check complete.",
        "Error occurred during processing.",
        150,
        -5,
        [],
        ["item1", "item2"]
    ]
    results = []
    for item in sample_inputs:
        category = categorize_input(item)
        results.append((item, category))
    for original, category in results:
        print(f"Input: {original}, Category: {category}")