class WeightExtractor:
    @staticmethod
    def extract_weights(data):
        weights = []
        if isinstance(data, dict):
            for key, value in data.items():
                weights.extend(WeightExtractor.extract_weights(value))
        elif isinstance(data, list):
            for item in data:
                weights.extend(WeightExtractor.extract_weights(item))
        elif isinstance(data, (int, float)):
            weights.append(data)
        return weights

if __name__ == '__main__':
    sample_data = {
        'user': {
            'personal_info': {
                'height': 175,
                'weight': 80
            },
            'medical_records': [
                {'date': '2023-01-01', 'weight': 78},
                {'date': '2023-01-02', 'notes': {'initial_weight': 79}}
            ]
        },
        'family_members': [
            {
                'name': 'parent',
                'weight': 65,
                'records': [
                    {'date': '2023-01-01', 'weight': 64},
                    {'date': '2023-01-02', 'notes': {'initial_weight': 63}}
                ]
            },
            {
                'name': 'sibling',
                'weight': 50,
                'records': [
                    {'date': '2023-01-01', 'weight': 49},
                    {'date': '2023-01-02', 'notes': {'initial_weight': 48}}
                ]
            }
        ]
    }
    
    weights = WeightExtractor.extract_weights(sample_data)
    print(weights)