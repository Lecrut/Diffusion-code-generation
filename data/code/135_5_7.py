def check_list_comprehensions():
    list_comp1 = [x**2 for x in range(5)]
    list_comp2 = [x*x for x in range(5)]
    return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    print(check_list_comprehensions())