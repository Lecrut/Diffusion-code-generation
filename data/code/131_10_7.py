import sys
def determine_category(input_value):
    if isinstance(input_value, str):
        lower_val = input_value.lower().strip()
        if lower_val.startswith("a"):
            return "Category A"
        elif lower_val.startswith("b"):
            return "Category B"
        elif lower_val.startswith("c"):
            return "Category C"
        else:
            return "Category D"
    elif isinstance(input_value, int):
        if input_value > 100:
            return "High Value"
        else:
            return "Low Value"
    else:
        return "Invalid Input Type"
if __name__ == '__main__':
    sample_inputs = [
        "Apple",
        "Banana",
        "Carrot",
        "Date",
        "150",
        "50",
        "Orange"
    ]
    for item in sample_inputs:
        result = determine_category(item)
        print(result)