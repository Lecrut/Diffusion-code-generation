import collections
def group_fruits(fruits):
    grouped = collections.defaultdict(list)
    for fruit in fruits:
        grouped[fruit].append(fruit)
    return dict(grouped)
if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = group_fruits(sample_fruits)
    print(result)