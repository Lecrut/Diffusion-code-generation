from typing import NamedTuple
import csv
from io import StringIO

class StoreEntry(NamedTuple):
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
        StoreEntry("Tech Innovations", "A store specializing in the latest technology gadgets."),
        StoreEntry("Book Haven", "Your one-stop shop for all types of books."),
        StoreEntry("Home Decor Hub", "Find unique and stylish home decor items here."),
        StoreEntry("Gourmet Galore", "Indulge in a variety of gourmet foods and beverages."),
        StoreEntry("Pet Paradise", "Care for your furry friends with the best pet supplies.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)