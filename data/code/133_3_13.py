import numpy as np

class QueryProcessor:
    def process_queries(self, queries):
        true_counts = np.sum(np.array(queries) == "True")
        return true_counts > len(queries) / 2

if __name__ == '__main__':
    processor = QueryProcessor()
    test_queries_1 = ["True", "False", "True", "False", "True"]
    print(f"Test 1: {processor.process_queries(test_queries_1)}")
    test_queries_2 = ["False", "False", "True", "False"]
    print(f"Test 2: {processor.process_queries(test_queries_2)}")
    test_queries_3 = ["True", "True", "False"]
    print(f"Test 3: {processor.process_queries(test_queries_3)}")