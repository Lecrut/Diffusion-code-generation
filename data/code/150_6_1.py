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
    else:
        return object_list
if __name__ == '__main__':
    object1 = GameObject("A")
    object2 = GameObject("B")
    object3 = GameObject("C")
    object4 = GameObject("D")
    original_list = [object1, object2, object3, object4]
    print("Original List:")
    print(original_list)
    print("-" * 20)
    target_to_remove = object2
    list_after_removal = remove_object_reference(original_list, target_to_remove)
    print(f"List after attempting to remove {target_to_remove}:")
    print(list_after_removal)
    print("-" * 20)
    target_not_present = GameObject("Z")
    list_after_no_removal = remove_object_reference(list_after_removal, target_not_present)
    print(f"List after attempting to remove {target_not_present}:")
    print(list_after_no_removal)
    print("-" * 20)
    list_comprehension_result = [obj for obj in original_list if obj is not target_to_remove]
    print(f"List after using list comprehension to remove {target_to_remove}:")
    print(list_comprehension_result)
    print("-" * 20)