class ObjectInstanceChecker:

    def __init__(self):
        self.instances = []

    def add_instance(self, obj):
        self.instances.append(obj)

    def check_presence(self, obj):
        return id(obj) in [id(instance) for instance in self.instances]
if __name__ == '__main__':
    checker = ObjectInstanceChecker()
    sample_obj1 = object()
    sample_obj2 = object()
    checker.add_instance(sample_obj1)
    print(checker.check_presence(sample_obj1))
    print(checker.check_presence(sample_obj2))