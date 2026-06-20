import json

class JsonComparator:
    def normalize_json(self, obj):
        if isinstance(obj, dict):
            return {self.normalize_json(k): self.normalize_json(v) for k, v in sorted(obj.items())}
        elif isinstance(obj, list):
            return [self.normalize_json(item) for item in obj]
        else:
            return obj

    def are_json_equivalent(self, json1, json2):
        normalized_json1 = self.normalize_json(json.loads(json1))
        normalized_json2 = self.normalize_json(json.loads(json2))
        return normalized_json1 == normalized_json2

if __name__ == '__main__':
    comparator = JsonComparator()
    sample_json1 = '{"b": 2, "a": 1}'
    sample_json2 = '{"a": 1, "b": 2}'
    print(comparator.are_json_equivalent(sample_json1, sample_json2))