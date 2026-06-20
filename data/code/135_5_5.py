def check_list_comprehensions(list_comp1, list_comp2):
    return set(eval(list_comp1)) == set(eval(list_comp2))

if __name__ == '__main__':
    sample_input = [x for x in range(5)]
    print(check_list_comprehensions("[x**2 for x in sample_input]", "[y**2 for y in sample_input]"))