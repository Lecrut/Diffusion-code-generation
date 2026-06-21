from operator import attrgetter

class CustomObject:
    def __init__(self, value):
        self.value = value

def sort_custom_objects(obj_list, attribute_name):
    return sorted(obj_list, key=attrgetter(attribute_name))

if __name__ == '__main__':
    sample_objects = [CustomObject(3), CustomObject(1), CustomObject(2)]
    sorted_objects = sort_custom_objects(sample_objects, 'value')
    print([obj.value for obj in sorted_objects])