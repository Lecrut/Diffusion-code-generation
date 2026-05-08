import copy
class GameObject:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"GameObject('{self.name}')"
def remove_object_reference(object_list, object_to_remove):
    new_list = []
    found = False
    for obj in object_list:
        if obj is object_to_remove:
            found = True
        else:
            new_list.append(obj)
    if found:
        return new_list
    else:
        return object_list
if __name__ == '__main__':
    object1 = GameObject("A")
    object2 = GameObject("B")
    object3 = GameObject("C")
    object4 = GameObject("D")
    object_list = [object1, object2, object3, object4]
    object_to_remove = object2
    print("Original list:")
    print(object_list)
    object_list_after_removal = remove_object_reference(object_list, object_to_remove)
    print("\nList after attempting to remove reference to object_to_remove:")
    print(object_list_after_removal)
    object_list_unchanged = remove_object_reference(object_list, object1)
    print("\nList after attempting to remove reference to object1 (which was present):")
    print(object_list_unchanged)
    object_list_no_change = remove_object_reference(object_list, GameObject("E"))
    print("\nList after attempting to remove reference to a non-existent object:")
    print(object_list_no_change)