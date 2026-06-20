def check_list_comprehensions():
    list_comp1 = [x**2 for x in range(10)]
    list_comp2 = [x*x for x in range(10)]
    return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    result = check_list_comprehensions()
    print(result)