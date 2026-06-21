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
        StoreEntry("Tech Innovations", "A leading tech store with the latest gadgets."),
        StoreEntry("Bookworms Corner", "Your one-stop for all kinds of books."),
        StoreEntry("Gourmet Galore", "Fresh and delicious food from around the world."),
        StoreEntry("Fashion Forward", "The newest trends in fashion and accessories."),
        StoreEntry("Pet Paradise", "Care for your furry friends with our wide selection.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)