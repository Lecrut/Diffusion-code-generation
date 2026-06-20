def compare_binary_objects(obj1, obj2):
    return obj1 if len(obj1) > len(obj2) else obj2

if __name__ == '__main__':
    binary_obj1 = b'\x00\x01\x02'
    binary_obj2 = b'\x00\x01'
    result = compare_binary_objects(binary_obj1, binary_obj2)
    print(result)