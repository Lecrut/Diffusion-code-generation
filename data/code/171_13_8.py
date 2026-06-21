from dataclasses import dataclass
import csv
from io import StringIO

@dataclass(frozen=True)
class Store:
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
        Store("Tech Innovations", "A store specializing in the latest technology gadgets."),
        Store("Book Haven", "Your one-stop shop for all types of books."),
        Store("Home Decor Hub", "Find unique and stylish home decor items here."),
        Store("Gourmet Groceries", "Fresh, organic, and gourmet foods at your fingertips."),
        Store("Pet Paradise", "All things pet-related: food, toys, and accessories.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)