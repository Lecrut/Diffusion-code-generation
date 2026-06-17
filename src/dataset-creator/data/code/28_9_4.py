import csv
import xml.etree.ElementTree as ET
from datetime import datetime
class AnimalManager:
    def __init__(self):
        self.animals = [
            {"name": "Lion", "category": "mammal", "location": "Savanna"},
            {"name": "Eagle", "category": "bird", "location": "Sky"},
            {"name": "Snake", "category": "reptile", "location": "Jungle"},
            {"name": "Whale", "category": "mammal", "location": "Ocean"},
            {"name": "Turtle", "category": "reptile", "location": "Beach"}
        ]
    def search_by_category(self, category):
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename="favorites.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category", "location"])
            writer.writeheader()
            for animal in self.animals:
                writer.writerow(animal)
    def export_to_xml(self, filename="favorites.xml"):
        root = ET.Element("AnimalCollection")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ET.SubElement(root, "timestamp").text = timestamp
        for animal in self.animals:
            animal_elem = ET.SubElement(root, "animal")
            name_elem = ET.SubElement(animal_elem, "name")
            category_elem = ET.SubElement(animal_elem, "category")
            location_elem = ET.SubElement(animal_elem, "location")
            name_elem.text = animal["name"]
            category_elem.text = animal["category"]
            location_elem.text = animal["location"]
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
if __name__ == '__main__':
    manager = AnimalManager()
    mammals = manager.search_by_category("mammal")
    print(f"Found {len(mammals)} animals in category 'mammal'")
    manager.export_to_csv("favorites.csv")
    manager.export_to_xml("favorites.xml")