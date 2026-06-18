def group_fruits(fruit_list):
    result = {}
    for fruit in fruit_list:
        if fruit not in result:
            result[fruit] = []
        result[fruit].append(fruit)
    return result
if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    grouped = group_fruits(sample_fruits)
    print(grouped)