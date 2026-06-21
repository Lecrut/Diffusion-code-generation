from typing import List, NamedTuple
import csv

class StoreEntry(NamedTuple):
    name: str
    description: str

def serialize_stores_to_csv(stores: List[StoreEntry]) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Description'])
    for store in stores:
        writer.writerow([store.name, store.description])
    return output.getvalue()

if __name__ == '__main__':
    sample_stores: List[StoreEntry] = [
        StoreEntry("Tech Innovations", "A hub for cutting-edge technology products."),
        StoreEntry("Bookworms Galore", "Your one-stop shop for all kinds of books."),
        StoreEntry("Gourmet Groceries", "Fresh and organic foods from around the world."),
        StoreEntry("Fashion Forward", "The latest in fashion and accessories."),
        StoreEntry("Pet Paradise", "All your pet's needs, from food to toys.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)