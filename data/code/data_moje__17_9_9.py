def extract_terminal_element(container):
    if len(container) == 0:
        return None
    index = len(container) - 1
    return container[index]

def categorize_item(value):
    labels = {
        10: "low",
        20: "medium",
        30: "high",
        40: "critical",
        50: "extreme"
    }
    return labels.get(value, "unknown")

if __name__ == '__main__':
    data_sequence = [10, 20, 30, 40, 50]
    last_val = extract_terminal_element(data_sequence)
    category = categorize_item(last_val)
    print(category)