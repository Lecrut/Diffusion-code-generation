START = 0
END = 10

def generate_list_comprehension(start, end, operation):
    return [operation(x) for x in range(start, end)]

def compare_comprehensions(list_comp1, list_comp2):
    return set(list_comp1) == set(list_comp2)

if __name__ == '__main__':
    operation = lambda x: x**2
    list_comp1 = generate_list_comprehension(START, END, operation)
    list_comp2 = generate_list_comprehension(START, END, operation)
    result = compare_comprehensions(list_comp1, list_comp2)
    print(result)