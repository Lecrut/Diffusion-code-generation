class JsonParser:
    @staticmethod
    def parse_value(value_str):
        try:
            return int(value_str)
        except ValueError:
            return value_str

    @classmethod
    def parse_json(cls, json_str):
        result = {}
        key, value = json_str.split(':')
        result[key.strip()] = cls.parse_value(value.strip())
        return result

if __name__ == '__main__':
    sample_string = "name:John Doe,age:30"
    parsed_data = JsonParser.parse_json(sample_string)
    print(parsed_data)