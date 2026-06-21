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
        StoreEntry('Store A', 'A small shop with unique items.'),
        StoreEntry('Store B', 'A very long and detailed description of this store.'),
        StoreEntry('Store C', 'Medium sized retail location.'),
        StoreEntry('Store D', 'Short description.'),
        StoreEntry('Store E', 'Another small store with a variety of products.')
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)