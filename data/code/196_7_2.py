if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_slice = list1 + list2
    concatenated_slicing = list1[:] + list2
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Concatenation using '+': {concatenated_slice}")
    print(f"Concatenation using slicing and '+': {concatenated_slicing}")