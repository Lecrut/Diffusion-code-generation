def process_list(data):
    if not data:
        return None
    return sum(data)
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = []
    list3 = [10, 20]
    result1 = process_list(list1)
    result2 = process_list(list2)
    result3 = process_list(list3)
    print(f"Result for {list1}: {result1}")
    print(f"Result for {list2}: {result2}")
    print(f"Result for {list3}: {result3}")