import csv
import xml.etree.ElementTree as ET
from typing import List, Dict
class AnimalManager:
    def __init__(self):
        self.animals = [
            {"name": "Lion", "category": "mammal", "habitat": "Savanna"},
            {"name": "Elephant", "category": "mammal", "habitat": "Jungle"},
            {"name": "Snake", "category": "reptile", "habitat": "Desert"},
            {"name": "Turtle", "category": "reptile", "habitat": "Ocean"},
            {"name": "Dog", "category": "mammal", "habitat": "Farm"}
        ]
    def search_by_category(self, category: str) -> List[Dict]:
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category", "habitat"])
            writer.writeheader()
            for animal in self.animals:
                writer.writerow(animal)
    def export_to_xml(self, filename: str):
        root = ET.Element("Animals")
        for animal in self.animals:
            elem = ET.SubElement(root, "Animal")
            name_elem = ET.SubElement(elem, "Name")
            category_elem = ET.SubElement(elem, "Category")
            habitat_elem = ET.SubElement(elem, "Habitat")
            name_elem.text = str(animal["name"])
            category_elem.text = animal["category"]
            habitat_elem.text = animal["habitat"]
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
if __name__ == '__main__':
    manager = AnimalManager()
    filtered_animals = manager.search_by_category("mammal")
    print(f"Found {len(filtered_animals)} mammals.")
    manager.export_to_csv("favorites.csv")
    manager.export_to_xml("favorites.xml")