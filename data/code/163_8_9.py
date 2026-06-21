def sort_fruits_by_color(fruits):
    return sorted(fruits, key=lambda fruit: fruit[1])

if __name__ == '__main__':
    fruits = [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple'), ('orange', 'orange')]
    print(sort_fruits_by_color(fruits))