import json

class JsonConstructor:
    def construct(self, name_value_pairs):
        return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    constructor = JsonConstructor()
    sample_data = {
        "name": "Jane Smith",
        "age": 28,
        "is_student": True,
        "major": "Computer Science"
    }
    print(constructor.construct(sample_data))