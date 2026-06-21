def custom_filter(predicate, elements):
    return [element for element in elements if not predicate(element)]

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    even_predicate = lambda num: num % 2 == 0
    filtered_numbers = custom_filter(even_predicate, numbers)
    print(filtered_numbers)