class ObjectList:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def contains(self, item):
        return id(item) in (id(obj) for obj in self.data)

if __name__ == '__main__':
    sample_object1 = object()
    sample_object2 = object()
    empty_list = ObjectList()

    list_object = ObjectList()
    list_object.add(sample_object1)
    list_object.add(sample_object2)

    print(f"Checking if {sample_object1} is in the list: {list_object.contains(sample_object1)}")
    print(f"Checking if {sample_object2} is in the list: {list_object.contains(sample_object2)}")
    print(f"Checking if {empty_list}: {list_object.contains(empty_list)}")