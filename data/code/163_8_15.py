def sort_fruits_by_color(fruit_color_pairs):
    if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in fruit_color_pairs):
        raise ValueError("All elements must be tuples of length 2")
    
    return sorted(fruit_color_pairs, key=lambda x: x[1])

if __name__ == '__main__':
    fruits = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    sorted_fruits = sort_fruits_by_color(fruits)
    print(sorted_fruits)