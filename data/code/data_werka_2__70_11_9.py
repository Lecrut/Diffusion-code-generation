def get_edge_elements(data):
    if len(data) == 0:
        raise ValueError("Input must be non-empty")
    return (data[0], data[-1])

class EdgeDataProcessor:
    def __init__(self, items):
        self.items = items

    def get_edges(self):
        return get_edge_elements(self.items)

    def get_edge_sum(self):
        edges = self.get_edges()
        return edges[0] + edges[1]

if __name__ == '__main__':
    sample_items = [10, 20, 30, 40, 50]
    processor = EdgeDataProcessor(sample_items)
    print(processor.get_edges())
    print(processor.get_edge_sum())