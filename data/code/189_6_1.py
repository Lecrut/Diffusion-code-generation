initial_list = [10, 20, 30, 40, 50]
item_to_remove = 30
list_with_remove = list(initial_list)
list_with_del = list(initial_list)
print("--- Testing .remove() ---")
print("Original List:", list_with_remove)
print("Item to remove:", item_to_remove)
try:
    list_with_remove.remove(item_to_remove)
    print("List after .remove():", list_with_remove)
except ValueError as e:
    print("Error during .remove():", e)
print("\n--- Testing del keyword ---")
print("Original List:", list_with_del)
del list_with_del[2]
print("List after del [2]:", list_with_del)
print("\n--- Performance Consideration (In-place vs Deletion) ---")
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_b = list(list_a)
print("List A initial:", list_a)
print("List B initial:", list_b)
list_c = list(list_a)
item_c = 5
try:
    list_c.remove(item_c)
except ValueError:
    pass
print("List C after .remove(5):", list_c)
list_d = list(list_a)
del list_d[4]
print("List D after del [4]:", list_d)
print("\nPerformance Summary:")
print("The .remove(value) operation requires a linear search (O(n)) to find the element before deletion.")
print("The del/pop operations, when using an index, are typically O(1) for direct deletion at that location.")
if __name__ == '__main__':
    pass