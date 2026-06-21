def sort_fruits_by_color(fruit_colors):
    return sorted(fruit_colors, key=lambda x: x[1])

if __name__ == '__main__':
    fruits = [('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')]
    print(sort_fruits_by_color(fruits))