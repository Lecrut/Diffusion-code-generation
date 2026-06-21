def sort_fruits_by_color(fruit_list):
    return sorted(fruit_list, key=lambda x: x[1])

if __name__ == '__main__':
    fruits = [("apple", "red"), ("banana", "yellow"), ("grape", "purple"), ("orange", "orange")]
    sorted_fruits = sort_fruits_by_color(fruits)
    print(sorted_fruits)