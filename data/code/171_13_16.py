from dataclasses import dataclass
import csv
from io import StringIO

@dataclass(frozen=True)
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
        StoreEntry("Tech Innovations", "A store for the latest technology gadgets."),
        StoreEntry("Book Haven", "Your one-stop shop for all types of books."),
        StoreEntry("Home Decor Hub", "Find everything you need to make your home beautiful."),
        StoreEntry("Gourmet Galore", "Fresh and delicious food from around the world."),
        StoreEntry("Pet Paradise", "Care for your furry friends with our wide selection.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)