import csv
import xml.etree.ElementTree as ET
from datetime import datetime
class AnimalManager:
    def __init__(self):
        self.animals = [
            {"name": "Lion", "category": "mammal", "habitat": "savanna"},
            {"name": "Snake", "category": "reptile", "habitat": "desert"},
            {"name": "Eagle", "category": "bird", "habitat": "sky"},
            {"name": "Shark", "category": "fish", "habitat": "ocean"},
            {"name": "Whale", "category": "mammal", "habitat": "ocean"}
        ]
    def search_by_category(self, category):
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename="favorites.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category", "habitat"])
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
            habitat_elem = ET.SubElement(animal_elem, "habitat")
            name_elem.text = animal["name"]
            category_elem.text = animal["category"]
            habitat_elem.text = animal["habitat"]
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
if __name__ == '__main__':
    manager = AnimalManager()
    print("Searching for mammals...")
    result_mammals = manager.search_by_category("mammal")
    for animal in result_mammals:
        print(f"Found: {animal['name']} ({animal['category']})")
    manager.export_to_csv()
    manager.export_to_xml()