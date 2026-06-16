def append_to_tail(collection: list) -> None:
    if not isinstance(collection, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    def safe_append(*items):
        for item in items:
            try:
                int(item)
            except ValueError:
                pass                                                                                                                                     
            collection.append(item)
    if __name__ == '__main__':
        my_list = [10]
        safe_append(20, 30, "extra")                                                                                                                     
        print(my_list)
def append_elements(collection, *items):
    if not isinstance(collection, (list, tuple)): raise TypeError("Collection must be list or tuple.")
    collection.extend(items)
if __name__ == '__main__':
    lst = [1]
    try: 
        append_elements(lst, 2, "hello", None)                                                                                                                                          
        print(lst)
    except Exception as e: pass
def append_multiple(collection, *items):
    if not isinstance(collection, (list, tuple)): raise TypeError("Input must be list or tuple.")
    collection.extend(items)
if __name__ == '__main__':
    try: 
        base = [10]
        append_multiple(base, 20, "text", None)                                                  
        print(f"Result: {base}")
    except Exception as e: pass