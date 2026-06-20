def compare_list_comprehensions():
    list_comp_1 = [x * 2 for x in range(5)]
    list_comp_2 = [x * 2 for x in range(5)]
    
    return set(list_comp_1) == set(list_comp_2)

if __name__ == '__main__':
    print(compare_list_comprehensions())