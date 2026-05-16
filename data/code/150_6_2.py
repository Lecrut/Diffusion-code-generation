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
    object_list = [object1, object2, object3, object4]
    print("Original list:")
    print(object_list)
    target_to_remove = object2
    print("\nAttempting to remove reference to:", target_to_remove.name)
    modified_list = remove_object_reference(object_list, target_to_remove)
    print("\nModified list after removal:")
    print(modified_list)
    print("\nOriginal list remains unchanged:")
    print(object_list)
    target_to_remove_2 = object1
    print("\nAttempting to remove reference to:", target_to_remove_2.name)
    modified_list_2 = remove_object_reference(object_list, target_to_remove_2)
    print("\nModified list after removal:")
    print(modified_list_2)