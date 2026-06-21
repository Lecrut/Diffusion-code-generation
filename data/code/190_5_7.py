class ObjectList:

    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def contains_object(self, obj):
        return obj in self.objects
if __name__ == '__main__':
    obj_list = ObjectList()
    sample_obj = object()
    obj_list.add_object(sample_obj)
    print(obj_list.contains_object(sample_obj))
    print(obj_list.contains_object(object()))