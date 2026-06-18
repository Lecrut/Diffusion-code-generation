import collections
fruits = ["apple", "banana", "cherry", "apple", "orange", "banana"]
grouped_fruits = collections.defaultdict(list)
for fruit in fruits:
    grouped_fruits[fruit].append(fruit)
if __name__ == '__main__':
    print(dict(grouped_fruits))