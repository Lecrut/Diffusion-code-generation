if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_slice = list1 + list2
    concatenated_slicing = list1 + list2
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"Concatenation using '+' operator: {concatenated_slice}")
    print(f"Concatenation using slicing (conceptually): {concatenated_slicing}")
    list3 = list1[:]                 
    list4 = list2[:]                 
    concatenated_slicing_explicit = list3 + list4
    print(f"Concatenation using explicit slicing and '+': {concatenated_slicing_explicit}")