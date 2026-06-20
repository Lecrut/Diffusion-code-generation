import numpy as np

class QueryProcessor:
    def __init__(self, queries):
        self.queries = np.array(queries, dtype=bool)

    def process_queries(self):
        return np.sum(self.queries) > len(self.queries) / 2

if __name__ == '__main__':
    processor1 = QueryProcessor(["True", "False", "True", "False"])
    print(processor1.process_queries())
    
    processor2 = QueryProcessor(["True", "True", "False", "False"])
    print(processor2.process_queries())
    
    processor3 = QueryProcessor(["True", "False", "False"])
    print(processor3.process_queries())