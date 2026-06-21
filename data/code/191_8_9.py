list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

def concatenate_lists(list_a, list_b):
    return list_a + list_b

if __name__ == '__main__':
    result = concatenate_lists(list1, list2)
    print(f"Combined List: {result}")