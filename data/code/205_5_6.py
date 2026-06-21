class CustomObject:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

def sort_custom_objects(obj_list):
    obj_list.sort(key=lambda x: x.get_value())
    return obj_list

if __name__ == '__main__':
    objects = [CustomObject(5), CustomObject(2), CustomObject(8), CustomObject(1), CustomObject(9), CustomObject(3)]
    sorted_objects = sort_custom_objects(objects)
    print("Sorted objects:", [(obj.get_value()) for obj in sorted_objects])