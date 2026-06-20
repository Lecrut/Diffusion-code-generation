def check_list_comprehensions(comp1, comp2):
    return set(comp1) == set(comp2)

if __name__ == '__main__':
    sample_comp1 = [x**3 for x in range(10)]
    sample_comp2 = [x*x*x for x in range(10)]
    result = check_list_comprehensions(sample_comp1, sample_comp2)
    print(result)