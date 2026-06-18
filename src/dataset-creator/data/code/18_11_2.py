def group_fruits(fruits):
    result = {}
    for fruit in fruits:
        if fruit not in result:
            result[fruit] = []
        result[fruit].append(fruit)
    return result
if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "apple", "orange", "banana", "grape"]
    grouped = group_fruits(sample_fruits)
    print(grouped)