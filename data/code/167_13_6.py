import json

def create_store_json():
    store_name = "Example Store"
    age = 5
    if not isinstance(age, int) or age <= 0:
        raise ValueError(f"Invalid age provided: {age}. Age must be a positive integer.")
    
    data = {
        "store_name": store_name,
        "age": age
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    try:
        print(create_store_json())
    except ValueError as e:
        print(e)