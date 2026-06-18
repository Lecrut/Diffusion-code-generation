from itertools import groupby
fruits = ["apple", "banana", "cherry", "apricot", "grape", "orange", "mango"]
fruit_types = {"apple": "pome", "banana": "berry", "cherry": "stone", "apricot": "stone", "grape": "berry", "orange": "citrus", "mango": "stone"}
sorted_fruits = sorted(fruits)
grouped_fruits = []
for fruit_type, group in groupby(sorted_fruits, key=lambda fruit: fruit_types[fruit]):
    grouped_fruits.append((fruit_type, list(group)))
if __name__ == '__main__':
    print(grouped_fruits)