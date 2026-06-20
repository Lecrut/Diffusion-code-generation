def compare_list_comprehensions():
    list_comp1 = [x**3 for x in range(5, 10)]
    list_comp2 = [x*x*x for x in range(5, 10)]
    return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    result = compare_list_comprehensions()
    print(result)