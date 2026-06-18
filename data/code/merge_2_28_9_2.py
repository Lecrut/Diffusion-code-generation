import csv
import xml.etree.ElementTree as ET
from datetime import datetime
class AnimalManager:
    def __init__(self):
        self.animals = [
            {"name": "Lion", "category": "mammal", "habitat": "Savanna"},
            {"name": "Snake", "category": "reptile", "habitat": "Desert"},
            {"name": "Eagle", "category": "bird", "habitat": "Sky"},
            {"name": "Whale", "category": "mammal", "habitat": "Ocean"},
            {"name": "Frog", "category": "amphibian", "habitat": "Jungle"}
        ]
    def search_by_category(self, category):
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename="favorites.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category", "habitat"])
            writer.writeheader()
            for animal in self.animals:
                writer.writerow(animal)
    def export_to_xml(self, filename="favorites.xml"):
        root = ET.Element("AnimalCollection")
        timestamp = ET.SubElement(root, "timestamp")
        timestamp.text = datetime.now().isoformat()
        for animal in self.animals:
            animal_elem = ET.SubElement(root, "animal")
            name_elem = ET.SubElement(animal_elem, "name")
            name_elem.text = animal["name"]
            category_elem = ET.SubElement(animal_elem, "category")
            category_elem.text = animal["category"]
            habitat_elem = ET.SubElement(animal_elem, "habitat")
            habitat_elem.text = animal["habitat"]
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
if __name__ == '__main__':
    manager = AnimalManager()
    filtered_animals = manager.search_by_category("mammal")
    print(f"Found {len(filtered_animals)} mammals.")
    manager.export_to_csv("favorites.csv")
    print("Exported to favorites.csv successfully.")
    manager.export_to_xml("favorites.xml")
    print("Exported to favorites.xml successfully.")