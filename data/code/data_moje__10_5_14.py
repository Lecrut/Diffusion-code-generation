class DictionaryInspector:
    @staticmethod
    def retrieve_first_value(data):
        if not data:
            return None
        value_iterator = iter(data.values())
        return next(value_iterator)

    @staticmethod
    def get_demo_dictionary():
        return {
            "alpha": 100,
            "beta": 200,
            "gamma": 300
        }

if __name__ == '__main__':
    sample_data = DictionaryInspector.get_demo_dictionary()
    result = DictionaryInspector.retrieve_first_value(sample_data)
    print(result)