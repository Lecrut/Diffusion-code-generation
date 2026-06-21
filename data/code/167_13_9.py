import json
STORE_NAMES = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
AGES = [25, 30, 15, 42, 5]

def create_store_json():
    data = {}
    for store_name, age in zip(STORE_NAMES, AGES):
        if isinstance(age, int) and age > 0:
            data[store_name] = age
        else:
            raise ValueError(f'Invalid age provided for {store_name}. Age must be a positive integer.')
    return json.dumps(data, indent=4)
if __name__ == '__main__':
    try:
        print(create_store_json())
    except ValueError as e:
        print(e)