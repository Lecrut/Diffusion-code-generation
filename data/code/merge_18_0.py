def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        if fruit in grouped:
            grouped[fruit].append(fruit)
        else:
            grouped[fruit] = [fruit]
    return grouped
if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Orange', 'Apple', 'Grape', 'Banana', 'Mango', 'Apple']
    result = group_fruits(fruits)
    print(result)