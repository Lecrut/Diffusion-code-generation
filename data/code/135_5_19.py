def compare_list_comprehensions(comp1, comp2):
    return set(eval(comp1)) == set(eval(comp2))

if __name__ == '__main__':
    sample_comp1 = "[x**2 for x in range(5)]"
    sample_comp2 = "[x*x for x in range(5)]"
    print(compare_list_comprehensions(sample_comp1, sample_comp2))