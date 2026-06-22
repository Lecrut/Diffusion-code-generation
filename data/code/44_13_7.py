def calculate_average(results):
    if not results:
        return 0.0
    total = sum(results)
    count = len(results)
    return total / count

if __name__ == '__main__':
    sample_results = [85, 92, 78, 95, 88]
    average = calculate_average(sample_results)
    print(average)