class MapMapper:
    def map(self, source_map, target_map):
        result_map = {}
        for key, value in source_map.items():
            if key in target_map:
                result_map[key] = target_map[key]
            else:
                result_map[key] = None
        return result_map
if __name__ == '__main__':
    source = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }
    target = {
        "a": 100,
        "b": 200,
        "e": 500
    }
    mapper = MapMapper()
    mapped_data = mapper.map(source, target)
    print(mapped_data)