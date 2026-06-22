import json

def convert_weights(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    converted_data = []
    for item in data:
        weight = item['weight']
        unit = item['unit']
        if unit == 'kg':
            pounds = weight * 2.20462
        elif unit == 'oz':
            pounds = weight / 16
        else:
            pounds = weight
        converted_data.append({'weight': pounds, 'unit': 'lbs'})
    
    with open('converted_weights.json', 'w') as file:
        json.dump(converted_data, file, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'weight': 10, 'unit': 'kg'},
        {'weight': 32, 'unit': 'oz'}
    ]
    with open('sample_weights.json', 'w') as file:
        json.dump(sample_data, file)
    
    convert_weights('sample_weights.json')