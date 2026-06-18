def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        if fruit not in grouped:
            grouped[fruit] = []
        grouped[fruit].append(fruit)
    return grouped
if __name__ == '__main__':
    sample_fruits = [
        'Apple', 'Banana', 'Orange', 'Apple', 'Grapes', 
        'Banana', 'Mango', 'Apple', 'Orange', 'Pineapple'
    ]
    result = group_fruits(sample_fruits)
    for fruit_type, fruits in result.items():
        print(f"{fruit_type}: {', '.join(sorted(list(set(fruits))))}")