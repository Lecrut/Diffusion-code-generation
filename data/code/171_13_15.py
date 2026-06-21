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
        StoreEntry('Store A', 'A great store with lots of items.'),
        StoreEntry('Store B', 'Another store offering a variety of products.'),
        StoreEntry('Store C', 'A small but charming store.'),
        StoreEntry('Store D', 'A store specializing in electronics.'),
        StoreEntry('Store E', 'An outdoor gear store.')
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)