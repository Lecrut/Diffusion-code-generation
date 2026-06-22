def calculate_average(results):
    if not results:
        return 0.0
    return sum(results) / len(results)

if __name__ == '__main__':
    sample_results = [85, 92, 78, 90, 88]
    average = calculate_average(sample_results)
    print(average)