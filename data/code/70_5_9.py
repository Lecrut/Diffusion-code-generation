class EdgeInspector:
    MIN_SIZE = 2

    def __init__(self, container):
        self.container = list(container)

    def get_boundary_values(self):
        if len(self.container) < self.MIN_SIZE:
            raise ValueError(f"Collection requires at least {self.MIN_SIZE} elements")
        start_index = 0
        end_index = -1
        return (self.container[start_index], self.container[end_index])

if __name__ == '__main__':
    inspector = EdgeInspector([100, 200, 300, 400, 500])
    boundary_values = inspector.get_boundary_values()
    print(boundary_values)