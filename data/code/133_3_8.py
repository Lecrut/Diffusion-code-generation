import numpy as np

def process_queries(queries):
    return np.array(queries).astype(bool)

if __name__ == '__main__':
    sample_queries = ['true', 'false', 'True', 'False']
    processed_results = process_queries(sample_queries)
    print(processed_results)