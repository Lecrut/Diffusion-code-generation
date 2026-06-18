def group_fruits(fruit_list):
    grouped_fruits = {}
    for fruit in fruit_list:
        fruit_type = fruit.split()[0]
        if fruit_type not in grouped_fruits:
            grouped_fruits[fruit_type] = []
        grouped_fruits[fruit_type].append(fruit)
    return grouped_fruits
if __name__ == '__main__':
    sample_fruits = [
        "Apple Red",
        "Banana Yellow",
        "Orange Sweet",
        "Apple Green",
        "Grape Purple",
        "Banana Green",
        "Orange Pink"
    ]
    grouped = group_fruits(sample_fruits)
    for fruit_type, fruits in grouped.items():
        print(f"--- {fruit_type}s ---")
        for fruit in fruits:
            print(f"- {fruit}")
        print()