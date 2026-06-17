def analyze_list(data):
    if not data:
        return None
    total = sum(data)
    count = len(data)
    product = 1
    for x in data:
        product *= x
    average = total / count
    maximum = max(data)
    minimum = min(data)
    return {
        "sum": total,
        "average": average,
        "product": product,
        "range": (maximum, minimum)
    }
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    results = analyze_list(sample_list)
    print(results)