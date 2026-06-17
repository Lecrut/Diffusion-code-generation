from typing import List, Dict
class FruitProcessor:
    def group_by_type(self) -> Dict[str, List[Dict]]:
        fruits = [
            {"name": "Apple", "biological_type": "Rosaceae"},
            {"name": "Banana", "biological_type": "Musaceae"},
            {"name": "Orange", "biological_type": "Rutaceae"},
            {"name": "Grape", "biological_type": "Vitaceae"},
            {"name": "Mango", "biological_type": "Anacardiaceae"},
        ]
        grouped = {}
        for fruit in fruits:
            type_key = fruit["biological_type"]
            if type_key not in grouped:
                grouped[type_key] = []
            grouped[type_key].append(fruit)
        return grouped
if __name__ == '__main__':
    processor = FruitProcessor()
    result = processor.group_by_type()
    for bio_type, fruit_list in sorted(result.items()):
        print(f"Biological Type: {bio_type}")
        fruits_in_group = list(map(lambda x: f"{x['name']} ({x.get('color', 'N/A')})", fruit_list))
        print(", ".join(fruits_in_group))