def count_items(sequence):
    return len(sequence)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = "hello"
    tuple1 = (10, 20, 30)
    string1 = "Python"
    empty_list = []
    empty_string = ""
    print(f"Count of {list1}: {count_items(list1)}")
    print(f"Count of '{list2}': {count_items(list2)}")
    print(f"Count of {tuple1}: {count_items(tuple1)}")
    print(f"Count of '{string1}': {count_items(string1)}")
    print(f"Count of {empty_list}: {count_items(empty_list)}")
    print(f"Count of '{empty_string}': {count_items(empty_string)}")