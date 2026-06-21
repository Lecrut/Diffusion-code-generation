fruits = [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple'), ('orange', 'orange')]

def sort_by_color(fruits):
    return sorted(fruits, key=lambda x: x[1])

if __name__ == '__main__':
    sorted_fruits = sort_by_color(fruits)
    print(sorted_fruits)