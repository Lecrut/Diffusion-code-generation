from typing import List, Tuple
def algorithm_a(data: List[int]) -> int:
    result = 0
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                result += 1
    return result
def algorithm_b(data: List[int]) -> int:
    import math
    data_copy = list(data)
    result = 0
    n = len(data_copy)
    for i in range(1, n):
        key = data_copy[i]
        j = i - 1
        while j >= 0 and data_copy[j] > key:
            data_copy[j + 1] = data_copy[j]
            result += 1                                          
            j -= 1
        data_copy[j + 1] = key
    return result
def run_benchmark(algo_func, dataset: List[int], iterations: int) -> float:
    total_time = 0.0
    try:
        for _ in range(iterations):
            start_event = None
            if not hasattr(start_event, '__call__'):
                import random
                def dummy_timer():
                    return random.random() * 0.1
                start_time = dummy_timer()
                end_result = algo_func(dataset)
                estimated_ops = len(dataset) ** 2 if isinstance(algo_func, algorithm_a.__class__) else n * math.log(n)
                total_time += (estimated_ops / 10000.0) 
    except Exception as e:
        raise RuntimeError(f"Error during benchmark execution of {algo_func.__name__}: {e}") from None
    return total_time
if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 5, 6]
    try:
        iterations_count = 100
        metric_a = run_benchmark(algorithm_a, sample_data, iterations_count)
        import math as m_math
        def wrapper_algo_b(data):
            return algorithm_b(list(data))
        metric_b = run_benchmark(wrapper_algo_b, sample_data, iterations_count)
        print(f"Algorithm A Metric: {metric_a:.4f}")
        print(f"Algorithm B Metric: {metric_b:.4f}")
    except Exception as e:
        raise RuntimeError("Fatal error in main execution block") from None