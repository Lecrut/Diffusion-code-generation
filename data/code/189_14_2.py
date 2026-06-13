def remove_and_del_example():
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    try:
        my_list.remove(30)
        print("After removing 30 using remove():", my_list)
        del my_list[1]
        print("After deleting element at index 1 using del: ", my_list)
        try:
            my_list.remove(99)
        except ValueError as e:
            print(f"Error caught: {e}")
            print("Attempted to remove non-existent item (99). List remains:", my_list)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    remove_and_del_example()