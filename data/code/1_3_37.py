class WeightExtractor:
    def __init__(self, data):
        self.data = data

    def extract(self):
        return list(self._recursive_extract(self.data))

    def _recursive_extract(self, d):
        if isinstance(d, dict):
            for key, value in d.items():
                yield from self._recursive_extract(value)
        elif isinstance(d, list):
            for item in d:
                yield from self._recursive_extract(item)
        elif isinstance(d, (int, float)):
            yield d

if __name__ == '__main__':
    sample_data = {
        'user': {
            'personal_info': {
                'height': 175,
                'weight': 80
            },
            'medical_records': [
                {'date': '2023-01-01', 'notes': {'initial_weight': 78}},
                {'date': '2023-01-02', 'weight': 79}
            ]
        },
        'family_members': [
            {
                'name': 'parent',
                'weight': 65,
                'children': [
                    {'name': 'child1', 'weight': 45},
                    {'name': 'child2', 'weight': 48}
                ]
            }
        ]
    }

    extractor = WeightExtractor(sample_data)
    weights = extractor.extract()
    print(weights)