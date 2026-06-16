def analyze_list(numbers):
    if not numbers:
        return None
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    product = 1
    for x in numbers:
        product *= x
    maximum = max(numbers)
    minimum = min(numbers)
    return {
        "sum": total_sum,
        "average": average,
        "product": product,
        "range": (minimum, maximum)
    }
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    results = analyze_list(sample_list)
    print(results)