def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        if fruit in grouped:
            grouped[fruit].append(1)
        else:
            grouped[fruit] = [1]
    return grouped
if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Apple', 'Orange', 'Banana', 'Apple', 'Grape']
    result = group_fruits(fruits)
    print(result)