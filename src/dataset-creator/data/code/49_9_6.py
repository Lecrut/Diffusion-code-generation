import time
def is_positive(result):
    return result > 0
def process_dataset(data_size=1_000_000):
    results = [time.time() + (i * 2) for i in range(1, data_size)]
    positive_count = sum(is_positive(r) for r in results)
    return {
        'total_processed': len(results),
        'positive_results': positive_count,
        'is_dataset_overall_positive': any(is_positive(r) for r in results)
    }
if __name__ == '__main__':
    start_time = time.perf_counter()
    result_data = process_dataset(data_size=500_000)
    end_time = time.perf_counter()
    print(f"Total processed: {result_data['total_processed']}")
    print(f"Positive results count: {result_data['positive_results']}")
    print(f"Dataset overall positive: {result_data['is_dataset_overall_positive']}")
    print(f"Execution time (seconds): {end_time - start_time:.4f}")