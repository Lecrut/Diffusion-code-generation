class Checklist:

    def __init__(self, items):
        self.items = set(items)

    def contains(self, item):
        return item in self.items
if __name__ == '__main__':
    checklist = Checklist(['apple', 'banana', 'cherry'])
    print(checklist.contains('banana'))
    print(checklist.contains('orange'))