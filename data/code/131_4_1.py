import numpy as np
def categorize_data(data_stream):
    categories = {
        "Low": lambda x: x <= 10,
        "Medium": lambda x: 10 < x <= 50,
        "High": lambda x: 50 < x <= 100,
        "Very_High": lambda x: x > 100
    }
    results = []
    for value in data_stream:
        if categories["Low"](value):
            results.append("Low")
        elif categories["Medium"](value):
            results.append("Medium")
        elif categories["High"](value):
            results.append("High")
        elif categories["Very_High"](value):
            results.append("Very_High")
        else:
            results.append("Error")
    return results
if __name__ == '__main__':
    sample_data = [5, 15, 33, 45, 60, 75, 99, 101, 50, 0, 100.5]
    categorized_results = categorize_data(sample_data)
    print(categorized_results)