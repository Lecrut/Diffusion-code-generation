import copy
class GameObject:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"GameObject('{self.name}')"
def remove_object_reference(object_list, target_object):
    new_list = []
    found = False
    for obj in object_list:
        if obj is target_object:
            found = True
        else:
            new_list.append(obj)
    if found:
        return new_list
    return object_list
if __name__ == '__main__':
    object1 = GameObject("A")
    object2 = GameObject("B")
    object3 = GameObject("C")
    object4 = GameObject("D")
    object_list = [object1, object2, object3, object4]
    target_to_remove = object2
    print("Original List:")
    print(object_list)
    list_after_removal = remove_object_reference(object_list, target_to_remove)
    print("\nList after removing reference to", target_to_remove.name)
    print(list_after_removal)
    print("\nOriginal List remains unchanged:")
    print(object_list)