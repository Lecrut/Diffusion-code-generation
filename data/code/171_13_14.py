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
        Store("Tech Innovations", "A place to buy the latest gadgets and tech accessories."),
        Store("Book Haven", "Your one-stop shop for all types of books."),
        Store("Home Decor Hub", "Find unique and stylish home decor items."),
        Store("Pet Paradise", "Care for your furry friends with our wide range of pet supplies."),
        Store("Gourmet Galore", "Indulge in delicious gourmet foods from around the world.")
    ]
    csv_output = serialize_stores_to_csv(sample_stores)
    print(csv_output)