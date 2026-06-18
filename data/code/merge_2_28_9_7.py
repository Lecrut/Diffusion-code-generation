import csv
import xml.etree.ElementTree as ET
class AnimalManager:
    def __init__(self):
        self.animals = [
            {"name": "Lion", "category": "mammal"},
            {"name": "Tiger", "category": "mammal"},
            {"name": "Snake", "category": "reptile"},
            {"name": "Frog", "category": "amphibian"},
            {"name": "Eagle", "category": "bird"}
        ]
    def search_by_category(self, category):
        return [animal for animal in self.animals if animal["category"].lower() == category.lower()]
    def export_to_csv(self, filename="favorites.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "category"])
            writer.writeheader()
            for animal in self.animals:
                writer.writerow(animal)
    def export_to_xml(self, filename="favorites.xml"):
        root = ET.Element("animal_collection")
        for animal in self.animals:
            elem = ET.SubElement(root, "animal")
            name_elem = ET.SubElement(elem, "name")
            name_elem.text = animal["name"]
            category_elem = ET.SubElement(elem, "category")
            category_elem.text = animal["category"]
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
if __name__ == '__main__':
    manager = AnimalManager()
    filtered_animals = manager.search_by_category("mammal")
    print(f"Found {len(filtered_animals)} mammals: {[a['name'] for a in filtered_animals]}")
    manager.export_to_csv()
    manager.export_to_xml()