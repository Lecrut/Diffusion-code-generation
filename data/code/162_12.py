class MapMapper:
    def convert(self, mapping: dict) -> dict:
        new_mapping = {}
        for key, value in mapping.items():
            new_mapping[key] = str(value)
        return new_mapping
if __name__ == '__main__':
    mapper = MapMapper()
    sample_data = {
        "name": 123,
        "age": "thirty",
        "is_active": True,
        "score": 99.5
    }
    result = mapper.convert(sample_data)
    print(result)