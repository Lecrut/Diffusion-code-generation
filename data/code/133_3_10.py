import numpy as np

def process_queries(queries):
    return np.array(queries)

if __name__ == '__main__':
    sample_queries = [True, False, True, True, False]
    processed_results = process_queries(sample_queries)
    print(processed_results)