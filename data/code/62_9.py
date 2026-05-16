my_list = ['a', 'b', 'c', 'd']
index_to_access = 1
direct_access = my_list[index_to_access]
print(f"Original list: {my_list}")
try:
    second_item_direct = my_list[1]
    print(f"Accessing the second item using direct indexing (list[1]): {second_item_direct}")
except IndexError:
    print("Direct indexing failed.")
try:
    second_item_safe = my_list.get(index_to_access)
    print(f"Accessing the second item using a conceptual .get() method (list.get(1)): {second_item_safe}")
except AttributeError:
    print("List objects do not natively support the .get() method for index lookup.")
except KeyError:
    print("KeyError encountered (not applicable for list indexing in this context).")
if __name__ == '__main__':
    pass