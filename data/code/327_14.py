def analyze_list(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    product = 1
    for x in numbers:
        product *= x
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    return {
        "sum": total,
        "average": average,
        "product": product,
        "range": (maximum, minimum)
    }
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    results = analyze_list(data)
    print(results)