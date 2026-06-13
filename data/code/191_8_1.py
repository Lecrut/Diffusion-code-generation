list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
combined_list = [x + y for x, y in zip(list1, list2)]
if __name__ == '__main__':
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Combined List (using zip and list comprehension): {combined_list}")