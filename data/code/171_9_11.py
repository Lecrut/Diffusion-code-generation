import csv

def serialize_stores_to_csv(stores):
    with open('stores.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for store in stores:
            writer.writerow(store)

if __name__ == '__main__':
    sample_stores = [
        {'name': 'Store A', 'description': 'Special offer on electronics!'},
        {'name': 'Store B', 'description': "Don't miss out on the latest gadgets."},
        {'name': 'Store C', 'description': 'Visit us for all your tech needs.'}
    ]
    
    serialize_stores_to_csv(sample_stores)