import csv
import xml.etree.ElementTree as ET
from typing import List, Dict
class AnimalManager:
    def __init__(self) -> None:
        self.animals = [
            {"name": "Lion", "category": "mammal"},
            {"name": "Tiger", "category": "mammal"},
            {"name": "Eagle", "category": "bird"},
            {"name": "Snake", "category": "reptile"},
            {"name": "Whale", "category": "mammal"}
        ]
    def search_by_category(self, category: str) -> List[Dict]:
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename: str = "favorites.csv") -> None:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category"])
            writer.writeheader()
            for animal in self.animals:
                writer.writerow(animal)
    def export_to_xml(self, filename: str = "favorites.xml") -> None:
        root = ET.Element("AnimalCollection")
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
    print("Mammals:", [a["name"] for a in manager.search_by_category("mammal")])
    manager.export_to_csv("animal_favorites.csv")
    manager.export_to_xml("animal_data.xml")