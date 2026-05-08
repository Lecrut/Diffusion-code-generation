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
    print("-" * 20)
    list_after_removal = remove_object_reference(object_list, target_to_remove)
    print("List after removing reference to object2:")
    print(list_after_removal)
    print("-" * 20)
    object_list_2 = [object1, object2, object3, object4]
    target_to_remove_2 = object1
    list_after_removal_2 = remove_object_reference(object_list_2, target_to_remove_2)
    print("Original List 2:")
    print(object_list_2)
    print("-" * 20)
    print("List 2 after removing reference to object1:")
    print(list_after_removal_2)
    print("-" * 20)
    object_list_3 = [object1, object2, object3, object4]
    target_to_remove_3 = GameObject("Z")
    list_after_removal_3 = remove_object_reference(object_list_3, target_to_remove_3)
    print("Original List 3:")
    print(object_list_3)
    print("-" * 20)
    print("List 3 after attempting to remove non-existent object Z:")
    print(list_after_removal_3)
    print("-" * 20)