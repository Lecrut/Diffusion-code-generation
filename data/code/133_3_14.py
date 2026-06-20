import numpy as np

def process_queries(queries):
    return np.array([q == 'true' for q in queries])

if __name__ == '__main__':
    sample_queries = ['true', 'false', 'true', 'true', 'false']
    print(process_queries(sample_queries))