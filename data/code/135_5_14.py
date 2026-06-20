def check_list_comprehensions(comp1, comp2):
    return set(comp1) == set(comp2)

if __name__ == '__main__':
    sample_comp1 = [x**4 for x in range(3, 8)]
    sample_comp2 = [x*x*x*x for x in range(3, 8)]
    result = check_list_comprehensions(sample_comp1, sample_comp2)
    print(result)