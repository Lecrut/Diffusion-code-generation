class Checklist:

    def __init__(self, items):
        self.items = set(items)

    def check(self, item):
        return item in self.items
if __name__ == '__main__':
    checklist = Checklist(['apple', 'banana', 'cherry'])
    print(checklist.check('banana'))
    print(checklist.check('orange'))