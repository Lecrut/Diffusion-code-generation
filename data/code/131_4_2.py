import numpy as np
def categorize_data(data_stream):
    categories = []
    for x in data_stream:
        if x < 10:
            category = "Low"
        elif 10 <= x < 50:
            category = "Medium"
        elif 50 <= x < 100:
            category = "High"
        else:
            category = "Very High"
        categories.append(category)
    return categories
if __name__ == '__main__':
    sample_data = [5, 15, 33, 49, 60, 99, 10, 50, 100, 0, 55, 9]
    categorized_results = categorize_data(sample_data)
    print(categorized_results)