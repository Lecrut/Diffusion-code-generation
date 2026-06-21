class Checklist:

    def __init__(self, items):
        self.items = frozenset(items)

    def is_member(self, item):
        return item in self.items
if __name__ == '__main__':
    checklist = Checklist([1, 2, 3, 4, 5])
    print(checklist.is_member(3))
    print(checklist.is_member(6))