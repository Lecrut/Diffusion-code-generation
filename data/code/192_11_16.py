class ListIntersector:
    def __init__(self, list_a, list_b):
        self.set_a = set(list_a)
        self.set_b = set(list_b)

    def get_intersection(self):
        return list(self.set_a.intersection(self.set_b))

if __name__ == '__main__':
    intersector = ListIntersector([1, 2, 3, 4, 2, 5], [4, 5, 6, 2, 1])
    result = intersector.get_intersection()
    print(result)