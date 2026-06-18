def parse_fruit_input(raw_string):
    return [fruit.strip().lower() for fruit in raw_string.split(',') if fruit.strip()]
def categorize_fruits(fruits_list, categories_config):
    grouped = {}
    citrus_items = [f for f in fruits_list if 'orange' in f or 'lemon' in f]
    grouped['Citrus'] = set(citrus_items)
    berry_items = [f for f in fruits_list if any(berry in f.lower() for berry in ['strawberry', 'blueberry', 'raspberry'])]
    grouped['Berries'] = set(berry_items)
    tropical_candidates = [f for f in fruits_list if any(trop in f.lower() for trop in ['mango', 'pineapple', 'papaya'])]
    return grouped
def main():
    sample_input = "Apple, Banana, Orange, Strawberry, Mango, Pineapple, Lemon"
    fruits_data = parse_fruit_input(sample_input)
    categories_config = {}                                                                                                   
    categorized_groups = categorize_fruits(fruits_data, {})
    print("Fruit Categories:")
    for category_name, items in categorized_groups.items():
        if items:
            sorted_items = sorted(list(items))
            print(f"{category_name}: {', '.join(sorted_items)}")
if __name__ == '__main__':
    main()