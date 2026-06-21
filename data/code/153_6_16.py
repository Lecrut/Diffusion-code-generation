ITEMS = ("apple", "banana", "cherry", "date")

def tuple_exists_in_list(target_tuple):
    return target_tuple in ITEMS

if __name__ == '__main__':
    sample_tuple = ("banana",)
    result = tuple_exists_in_list(sample_tuple)
    print(result)