import json

class JSONBuilder:
    def build(self, name_value_pairs):
        return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    builder = JSONBuilder()
    sample_data = {
        "name": "Jane Smith",
        "age": 25,
        "is_student": True,
        "major": "Computer Science"
    }
    print(builder.build(sample_data))