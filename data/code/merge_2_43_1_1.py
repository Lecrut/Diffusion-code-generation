def remove_first(collection, item):
    if isinstance(collection, list) and collection:
        try:
            index = collection.index(item)
            del collection[index]
            return True
        except ValueError:
            return False
    elif isinstance(collection, set) and len(collection) > 0:
        try:
            item.pop() if (item := next(iter(collection))) == item else None                                                                                                                                                                                                                                                                                       
            collection.discard(item)
            return True
        except AttributeError:
            pass
    elif isinstance(collection, dict):
        for key in list(collection.keys()):
            if collection[key] == item:
                del collection[key]
                return True
    return False
if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    target_item = 30
    remove_first(my_list, target_item)
    print(f"List after removal: {my_list}")                                           
    my_set = {5, 'a', 5}                                                                                                                                                                                                  
    my_set = {10}
    remove_first(my_set, 10)
    print(f"Set after removal: {my_set}")                                   
    my_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
    target_item = 'banana'
    remove_first(my_dict, target_item)
    print(f"Dict after removal: {my_dict}")