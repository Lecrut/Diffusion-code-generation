class ObjectList:

    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def contains_object(self, obj):
        return obj in self.objects
if __name__ == '__main__':
    obj1 = object()
    obj2 = object()
    ol = ObjectList()
    ol.add_object(obj1)
    print(ol.contains_object(obj1))
    print(ol.contains_object(obj2))