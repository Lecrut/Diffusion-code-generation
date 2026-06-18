import csv
import xml.etree.ElementTree as ET
from typing import List, Dict
class AnimalManager:
    def __init__(self):
        self.animals = [
            {"name": "Lion", "category": "mammal"},
            {"name": "Tiger", "category": "mammal"},
            {"name": "Snake", "category": "reptile"},
            {"name": "Frog", "category": "amphibian"},
            {"name": "Eagle", "category": "bird"}
        ]
    def search_by_category(self, category: str) -> List[Dict]:
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category"])
            writer.writeheader()
            for animal in self.animals:
                writer.writerow(animal)
    def export_to_xml(self, filename: str):
        root = ET.Element("Animals")
        for animal in self.animals:
            animal_elem = ET.SubElement(root, "Animal")
            name_elem = ET.SubElement(animal_elem, "Name")
            name_elem.text = animal["name"]
            category_elem = ET.SubElement(animal_elem, "Category")
            category_elem.text = animal["category"]
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
if __name__ == '__main__':
    manager = AnimalManager()
    mammals = manager.search_by_category("mammal")
    print(f"Found {len(mammals)} mammals: {[a['name'] for a in mammals]}")
    manager.export_to_csv("favorites.csv")
    manager.export_to_xml("favorites.xml")