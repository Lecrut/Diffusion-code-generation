def sort_fruits_by_color(fruit_colors):
    return sorted(fruit_colors, key=lambda fruit: fruit[1])

if __name__ == '__main__':
    fruits = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    sorted_fruits = sort_fruits_by_color(fruits)
    print(sorted_fruits)