from dataclasses import dataclass
import csv
from io import StringIO

@dataclass
class StoreEntry:
    name: str
    description: str

def serialize_stores_to_csv(stores):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Description'])
    for store in stores:
        writer.writerow([store.name, store.description])
    return output.getvalue()

if __name__ == '__main__':
    sample_stores = [
        StoreEntry("Tech Innovations", "A place for the latest gadgets and tech accessories."),
        StoreEntry("Bookworms Corner", "Your one-stop shop for all types of books."),
        StoreEntry("Fresh Bites Market", "Savor fresh fruits, vegetables, and prepared meals."),
        StoreEntry("Pet Paradise", "Care for your furry friends with a variety of pet supplies."),
        StoreEntry("Gadget Galaxy", "Explore the universe of electronics and gadgets.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)