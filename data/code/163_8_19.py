FRUIT_COLOR_TUPLES = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]

def sort_by_color(fruit_color_list):
    return sorted(fruit_color_list, key=lambda x: x[1])

if __name__ == '__main__':
    sorted_fruits = sort_by_color(FRUIT_COLOR_TUPLES)
    print(sorted_fruits)