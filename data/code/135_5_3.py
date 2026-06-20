def are_list_comprehensions_equal(comp1, comp2):
    return set(comp1) == set(comp2)

if __name__ == '__main__':
    sample_comp1 = [x**2 for x in range(5)]
    sample_comp2 = [x*x for x in range(5)]
    result = are_list_comprehensions_equal(sample_comp1, sample_comp2)
    print(result)