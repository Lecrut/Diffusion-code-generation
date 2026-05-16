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
    object1 = GameObject("Apple")
    object2 = GameObject("Banana")
    object3 = GameObject("Cherry")
    object4 = GameObject("Date")
    original_list = [object1, object2, object3, object4]
    print("Original List:")
    print(original_list)
    object_to_remove = object2
    print("\nAttempting to remove reference to:", object_to_remove)
    list_after_removal = remove_object_reference(original_list, object_to_remove)
    print("\nList after removal:")
    print(list_after_removal)
    list_after_removal_attempt2 = remove_object_reference(original_list, object1)
    print("\nList after removing object1:")
    print(list_after_removal_attempt2)