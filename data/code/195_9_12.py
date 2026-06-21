import hashlib

def lists_equal_by_hash(list1, list2):
    if len(list1) != len(list2):
        return False
    hash_list1 = hashlib.sha256(str(list1).encode()).hexdigest()
    hash_list2 = hashlib.sha256(str(list2).encode()).hexdigest()
    return hash_list1 == hash_list2
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    print(lists_equal_by_hash(list1, list2))
    list3 = [1, 2, 3, 4, 6]
    print(lists_equal_by_hash(list1, list3))