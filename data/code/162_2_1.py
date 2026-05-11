class MapMapper:
    def map(self, source_map: dict, target_map: dict) -> dict:
        result_map = {}
        for key, value in source_map.items():
            if key in target_map:
                result_map[key] = value
        return result_map
if __name__ == '__main__':
    source = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    target = {
        "a": "one",
        "b": "two",
        "e": "five"
    }
    mapper = MapMapper()
    mapped_data = mapper.map(source, target)
    print(mapped_data)