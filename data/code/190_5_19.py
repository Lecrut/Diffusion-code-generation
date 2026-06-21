class ObjectInstanceChecker:

    def __init__(self):
        self.instances = []

    def add_instance(self, obj):
        self.instances.append(obj)

    def contains_instance(self, obj):
        return id(obj) in [id(i) for i in self.instances]
if __name__ == '__main__':
    checker = ObjectInstanceChecker()
    obj1 = object()
    obj2 = object()
    checker.add_instance(obj1)
    print(checker.contains_instance(obj1))
    print(checker.contains_instance(obj2))