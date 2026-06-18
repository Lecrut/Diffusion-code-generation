import statistics
def compute_stats(values):
    try:
        if not all(isinstance(x, (int, float)) for x in values):
            raise ValueError("All elements must be numeric.")
        avg = statistics.mean(values)
        stdev = statistics.stdev(values)
        return {"average": round(avg, 2), "standard_deviation": round(stdev, 2)}
    except Exception as e:
        return {"error": str(e)}
def main():
    datasets = [10.5, 11.0, 9.8], [7.2, 6.9, 7.4]
    for dataset in datasets:
        result = compute_stats(dataset)
        if "error" not in result:
            print(f"Dataset {dataset}: Average={result['average']}, StdDev={result['standard_deviation']}")
if __name__ == '__main__':
    main()