def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        fruit_type = "unknown"
        if "apple" in fruit or "orange" in fruit:
            fruit_type = "citrus"
        elif "banana" in fruit or "grape" in fruit:
            fruit_type = "tropical"
        elif "strawberry" in fruit or "blueberry" in fruit:
            fruit_type = "berry"
        else:
            fruit_type = "other"
        if fruit_type not in grouped:
            grouped[fruit_type] = []
        grouped[fruit_type].append(fruit)
    return grouped
if __name__ == '__main__':
    input_fruits = [
        "apple",
        "orange",
        "banana",
        "grape",
        "strawberry",
        "blueberry",
        "mango",
        "kiwi"
    ]
    result = group_fruits(input_fruits)
    print(result)