import numpy as np
def categorize_data(data_stream):
    categories = []
    for x in data_stream:
        if x < 10:
            categories.append("Category_A")
        elif 10 <= x < 50:
            categories.append("Category_B")
        elif 50 <= x < 100:
            categories.append("Category_C")
        else:
            categories.append("Category_D")
    return categories
if __name__ == '__main__':
    sample_data = [5, 15, 33, 49, 60, 99, 10, 50, 100, 0, 55, 25]
    categorized_results = categorize_data(sample_data)
    print(categorized_results)