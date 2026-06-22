class EndpointAnalyzer:
    def __init__(self, collection):
        self.collection = list(collection)

    def _validate_length(self):
        size = len(self.collection)
        if size < 2:
            raise ValueError("Collection must have at least two items")

    def get_boundary_values(self):
        self._validate_length()
        start_index = 0
        end_index = -1
        return (self.collection[start_index], self.collection[end_index])

if __name__ == '__main__':
    analyzer = EndpointAnalyzer([100, 200, 300, 400])
    boundaries = analyzer.get_boundary_values()
    print(boundaries)